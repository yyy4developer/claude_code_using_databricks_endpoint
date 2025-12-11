# Databricks セットアップ手順

このドキュメントでは、Claude CodeでDatabricksエンドポイントを使用するために必要なDatabricks側の設定手順を説明します。

## 前提条件

- Databricksワークスペースへのアクセス権限
- 管理者権限（エンドポイントの確認に必要）

## ステップ1: Personal Access Token (PAT) の発行

### 1.1 Databricksワークスペースにログイン

ブラウザでDatabricksワークスペースにアクセスしてログインします。

### 1.2 ユーザー設定を開く

1. 右上のユーザー名をクリック
2. 「Settings」を選択

### 1.3 Access Tokensタブを開く

1. 左側のメニューから「Access Tokens」を選択
2. 「Generate New Token」ボタンをクリック

### 1.4 トークンを生成

1. **Comment**: トークンの説明を入力（例: "Claude Code用"）
2. **Lifetime**: トークンの有効期限を設定
   - 推奨: 90日以上（本番環境では適切な期間を設定）
3. 「Generate」ボタンをクリック

### 1.5 トークンをコピー

**重要**: トークンは一度しか表示されません。必ずコピーして安全な場所に保存してください。

トークンの形式: `dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

## ステップ2: Base URLの確認

### 2.1 ワークスペースURLを確認

DatabricksワークスペースのURLを確認します。

URLの形式: `https://<workspace-name>.cloud.databricks.com`

例: `https://e2-demo-field-eng.cloud.databricks.com`

### 2.2 Serving Endpointsの確認

1. Databricksワークスペースで左側のメニューから「Serving」を選択
2. 使用するエンドポイント名を確認

例: `databricks-claude-sonnet-4-5`

### 2.3 Base URLの構築

Base URLは以下の形式で構築されます：

```
https://<workspace-name>.cloud.databricks.com/serving-endpoints/anthropic
```

例: `https://e2-demo-field-eng.cloud.databricks.com/serving-endpoints/anthropic`

**注意**: エンドポイント名はBase URLには含まれません。エンドポイント名は別途設定ファイルで指定します。

## ステップ3: エンドポイントの状態確認

エンドポイントがReady状態であることを確認します：

1. Databricksワークスペースで「Serving」を開く
2. 使用するエンドポイントを選択
3. 状態が「Ready」であることを確認

## 必要な情報のまとめ

以下の情報をメモしておいてください：

- **PAT (Personal Access Token)**: `dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- **Base URL**: `https://<workspace-name>.cloud.databricks.com/serving-endpoints/anthropic`
- **エンドポイント名**: `databricks-claude-sonnet-4-5`（使用するエンドポイント名）

これらの情報は、次のステップで設定ファイル（`~/.claude/settings.json`）に設定します。

## 次のステップ

Databricks側の設定が完了したら、以下の手順に進んでください：

1. **設定ファイルの編集**: [SETTINGS.md](./SETTINGS.md)を参照
2. **疎通確認**: `python3 test_connection.py`を実行

