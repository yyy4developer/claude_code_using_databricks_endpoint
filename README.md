# Claude Code with Databricks

Claude CodeをDatabricksのServing Endpoints経由で使用するためのセットアップガイドです。

## 前提条件

- **Python**: 3.8以上
- **Node.js**: 18以上（推奨: 20以上）
- **requestsライブラリ**: 疎通確認スクリプトで使用

### Python依存関係のインストール

疎通確認スクリプト（`test_connection.py`）を使用する場合は、`requests`ライブラリをインストールしてください：

```bash
pip install requests
```

## クイックスタート

1. **Claude Codeのインストール**: [INSTALL.md](./INSTALL.md)を参照
2. **Databricks側の設定**: [DATABRICKS_SETUP.md](./DATABRICKS_SETUP.md)を参照
3. **設定ファイルの編集**: [SETTINGS.md](./SETTINGS.md)を参照
4. **疎通確認**: `python3 test_connection.py`を実行

## 必要な手順

### 1. Claude Codeのインストール

```bash
npm install -g @anthropic-ai/claude-code
```

詳細は [INSTALL.md](./INSTALL.md) を参照してください。

### 2. Databricks側の設定

- Personal Access Token (PAT) の発行
- Base URLの確認
- エンドポイント名の確認

詳細は [DATABRICKS_SETUP.md](./DATABRICKS_SETUP.md) を参照してください。

### 3. 設定ファイルの編集

`~/.claude/settings.json` を編集して、Databricksの設定を追加します。

詳細は [SETTINGS.md](./SETTINGS.md) を参照してください。

### 4. 疎通確認

```bash
python3 test_connection.py
```

## 使用方法

### 対話モード

```bash
claude
```

### 非対話モード

```bash
claude -p "Hello, Claude!"
```

## ドキュメント

- [INSTALL.md](./INSTALL.md) - Claude Codeのインストール手順
- [DATABRICKS_SETUP.md](./DATABRICKS_SETUP.md) - Databricks側の設定手順
- [SETTINGS.md](./SETTINGS.md) - settings.jsonの設定手順

## トラブルシューティング

設定に問題がある場合は、`test_connection.py`を実行してエラーメッセージを確認してください。

各ドキュメントにもトラブルシューティングセクションが含まれています。
