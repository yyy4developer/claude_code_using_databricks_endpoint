#!/usr/bin/env python3
"""
Claude Code設定の疎通確認スクリプト

このスクリプトは、~/.claude/settings.jsonの設定が正しく動作するか確認します。

使用方法:
    python3 test_connection.py
"""

import os
import json
import sys
from pathlib import Path

def load_settings():
    """設定ファイルから設定を読み込む"""
    settings_path = Path.home() / ".claude" / "settings.json"
    
    if not settings_path.exists():
        print(f"❌ 設定ファイルが見つかりません: {settings_path}")
        print("   設定ファイルを作成してください。詳しくは SETTINGS.md を参照してください。")
        return None
    
    try:
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        return settings
    except json.JSONDecodeError as e:
        print(f"❌ 設定ファイルのJSON構文エラー: {e}")
        return None
    except Exception as e:
        print(f"❌ 設定ファイルの読み込みエラー: {e}")
        return None

def get_config(settings):
    """設定ファイルから設定を取得"""
    if not settings or 'env' not in settings:
        print("❌ 設定ファイルに 'env' セクションが見つかりません。")
        return None
    
    env = settings['env']
    
    config = {
        'base_url': env.get('ANTHROPIC_BASE_URL'),
        'auth_token': env.get('ANTHROPIC_AUTH_TOKEN'),
        'model': env.get('ANTHROPIC_MODEL')
    }
    
    # 必須項目の確認
    missing = []
    if not config['base_url']:
        missing.append("ANTHROPIC_BASE_URL")
    if not config['auth_token']:
        missing.append("ANTHROPIC_AUTH_TOKEN")
    if not config['model']:
        missing.append("ANTHROPIC_MODEL")
    
    if missing:
        print("❌ 設定が不完全です。以下の項目が設定されていません:")
        for item in missing:
            print(f"   - {item}")
        print("\n詳しくは SETTINGS.md を参照してください。")
        return None
    
    return config

def test_connection(config):
    """Databricksエンドポイントへの接続をテスト"""
    try:
        import requests
    except ImportError:
        print("❌ requestsライブラリがインストールされていません。")
        print("   以下のコマンドでインストールしてください:")
        print("   pip install requests")
        return False
    
    base_url = config['base_url'].rstrip('/')
    auth_token = config['auth_token']
    model = config['model']
    
    # Base URLからワークスペースURLを抽出
    # 例: https://workspace.cloud.databricks.com/serving-endpoints/anthropic
    # -> https://workspace.cloud.databricks.com
    workspace_url = base_url.replace('/serving-endpoints/anthropic', '')
    
    # エンドポイントの状態を確認するAPI
    api_url = f"{workspace_url}/api/2.0/serving-endpoints/{model}"
    
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    print(f"\n🔍 接続テストを開始します...")
    print(f"   Workspace URL: {workspace_url}")
    print(f"   Endpoint: {model}")
    print(f"   Base URL: {base_url}")
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            endpoint_info = response.json()
            # レスポンス構造に応じて状態を取得
            state = 'UNKNOWN'
            if isinstance(endpoint_info, dict):
                if 'state' in endpoint_info:
                    state_obj = endpoint_info['state']
                    if isinstance(state_obj, dict):
                        if 'config_update' in state_obj:
                            config_update = state_obj['config_update']
                            if isinstance(config_update, dict) and 'state' in config_update:
                                state = config_update['state']
                        elif 'state' in state_obj:
                            state = state_obj['state']
                    elif isinstance(state_obj, str):
                        state = state_obj
                elif 'status' in endpoint_info:
                    state = endpoint_info['status']
            
            print(f"\n✅ 接続成功!")
            print(f"   エンドポイント状態: {state}")
            
            # Claude Code CLIのテスト
            print(f"\n🔍 Claude Code CLIのテスト...")
            try:
                import subprocess
                result = subprocess.run(
                    ['claude', '--version'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    print(f"   ✅ Claude Code CLIが利用可能です")
                    print(f"   バージョン: {result.stdout.strip()}")
                else:
                    print(f"   ⚠️  Claude Code CLIのバージョン確認に失敗しました")
            except FileNotFoundError:
                print(f"   ⚠️  Claude Code CLIが見つかりません")
                print(f"   インストール手順は INSTALL.md を参照してください。")
            except Exception as e:
                print(f"   ⚠️  Claude Code CLIの確認中にエラー: {e}")
            
            return True
        elif response.status_code == 401:
            print(f"\n❌ 認証エラー (401)")
            print("   PATの有効期限または権限を確認してください。")
            print("   DATABRICKS_SETUP.md を参照してPATを再発行してください。")
            return False
        elif response.status_code == 404:
            print(f"\n❌ エンドポイントが見つかりません (404)")
            print(f"   エンドポイント名 '{model}' が正しいか確認してください。")
            print("   DATABRICKS_SETUP.md を参照してエンドポイント名を確認してください。")
            return False
        else:
            print(f"\n❌ エラー: HTTP {response.status_code}")
            print(f"   レスポンス: {response.text[:200]}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"\n❌ 接続エラー")
        print("   ネットワーク接続またはホストURLを確認してください。")
        print(f"   Base URL: {base_url}")
        return False
    except requests.exceptions.Timeout:
        print(f"\n❌ タイムアウトエラー")
        print("   ネットワーク接続を確認してください。")
        return False
    except Exception as e:
        print(f"\n❌ 予期しないエラー: {e}")
        return False

def main():
    """メイン関数"""
    print("=" * 60)
    print("Claude Code 設定 疎通確認")
    print("=" * 60)
    
    # 設定ファイルの読み込み
    settings = load_settings()
    if not settings:
        sys.exit(1)
    
    # 設定の取得
    config = get_config(settings)
    if not config:
        sys.exit(1)
    
    # 接続テスト
    success = test_connection(config)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ すべてのテストが成功しました!")
        print("   Claude CodeでDatabricksエンドポイントを使用できます。")
        print("\n使用方法:")
        print("   claude                    # 対話モード")
        print("   claude -p \"Hello\"        # 非対話モード")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("❌ テストが失敗しました。")
        print("   設定を確認してください。")
        print("\n確認事項:")
        print("   1. SETTINGS.md で設定ファイルの内容を確認")
        print("   2. DATABRICKS_SETUP.md でPATとBase URLを確認")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()

