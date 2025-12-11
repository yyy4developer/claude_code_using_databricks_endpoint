# settings.json 設定手順

このドキュメントでは、Claude CodeでDatabricksエンドポイントを使用するための設定ファイル（`~/.claude/settings.json`）の編集方法を説明します。

## 設定ファイルの場所

設定ファイルは以下の場所に配置されます：

```
~/.claude/settings.json
```

macOS/Linuxの場合、フルパスは：
```
/home/ユーザー名/.claude/settings.json
```

## 設定ファイルの作成

### ステップ1: ディレクトリの作成

設定ファイルを配置するディレクトリが存在しない場合は作成します：

```bash
mkdir -p ~/.claude
```

### ステップ2: 設定ファイルの作成

設定ファイルを作成または編集します：

```bash
# エディタで開く（例: vim）
vim ~/.claude/settings.json

# または、nanoエディタを使用
nano ~/.claude/settings.json
```

## 設定ファイルの内容

以下の形式で設定ファイルを作成します：

```json
{
  "env": {
    "ANTHROPIC_MODEL": "databricks-claude-sonnet-4-5",
    "ANTHROPIC_BASE_URL": "https://your-workspace.cloud.databricks.com/serving-endpoints/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "databricks-claude-opus-4-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "databricks-claude-sonnet-4-5"
  },
  "alwaysThinkingEnabled": false
}
```

## 各設定項目の説明

### ANTHROPIC_MODEL

使用するデフォルトのモデル名を指定します。

例: `"databricks-claude-sonnet-4-5"`

### ANTHROPIC_BASE_URL

DatabricksのServing EndpointsのBase URLを指定します。

形式: `https://<workspace-name>.cloud.databricks.com/serving-endpoints/anthropic`

例: `"https://your-workspace.cloud.databricks.com/serving-endpoints/anthropic"`

### ANTHROPIC_AUTH_TOKEN

Databricksで発行したPersonal Access Token (PAT)を指定します。

形式: `dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

**重要**: このトークンは機密情報です。GitHubなどにコミットしないでください。

### ANTHROPIC_DEFAULT_OPUS_MODEL

Opusモデルを使用する場合のデフォルトモデル名を指定します。

例: `"databricks-claude-opus-4-5"`

### ANTHROPIC_DEFAULT_SONNET_MODEL

Sonnetモデルを使用する場合のデフォルトモデル名を指定します。

例: `"databricks-claude-sonnet-4-5"`

### alwaysThinkingEnabled

思考プロセスの表示を有効にするかどうかを指定します。

- `false`: 思考プロセスを表示しない（デフォルト）
- `true`: 思考プロセスを表示する

## 設定例

### 例1: Sonnetモデルのみを使用

```json
{
  "env": {
    "ANTHROPIC_MODEL": "databricks-claude-sonnet-4-5",
    "ANTHROPIC_BASE_URL": "https://your-workspace.cloud.databricks.com/serving-endpoints/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "databricks-claude-sonnet-4-5"
  },
  "alwaysThinkingEnabled": false
}
```

### 例2: OpusモデルとSonnetモデルの両方を設定

```json
{
  "env": {
    "ANTHROPIC_MODEL": "databricks-claude-sonnet-4-5",
    "ANTHROPIC_BASE_URL": "https://your-workspace.cloud.databricks.com/serving-endpoints/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "databricks-claude-opus-4-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "databricks-claude-sonnet-4-5"
  },
  "alwaysThinkingEnabled": false
}
```

## 設定ファイルの確認

設定ファイルが正しく作成されたか確認します：

```bash
# 設定ファイルの内容を確認
cat ~/.claude/settings.json

# JSON形式が正しいか確認
cat ~/.claude/settings.json | python3 -m json.tool
```

JSON形式が正しくない場合は、エラーメッセージが表示されます。

## トラブルシューティング

### 設定ファイルが見つからない

**問題**: `設定ファイルが見つかりません`

**解決方法**:
1. ディレクトリが存在するか確認: `ls -la ~/.claude/`
2. 設定ファイルが存在するか確認: `ls -la ~/.claude/settings.json`
3. 存在しない場合は作成: `mkdir -p ~/.claude && touch ~/.claude/settings.json`

### JSON形式エラー

**問題**: `JSON構文エラー`

**解決方法**:
1. JSON形式が正しいか確認: `cat ~/.claude/settings.json | python3 -m json.tool`
2. カンマや引用符が正しく使用されているか確認
3. オンラインJSONバリデーターを使用して検証

### 認証エラー

**問題**: `認証エラー (401)`

**解決方法**:
1. `ANTHROPIC_AUTH_TOKEN`が正しいか確認
2. PATの有効期限を確認
3. PATに適切な権限があるか確認

### エンドポイントが見つからない

**問題**: `エンドポイントが見つかりません (404)`

**解決方法**:
1. `ANTHROPIC_BASE_URL`が正しいか確認
2. `ANTHROPIC_MODEL`（エンドポイント名）が正しいか確認
3. Databricksワークスペースでエンドポイントが存在するか確認

## 次のステップ

設定ファイルの編集が完了したら、以下の手順に進んでください：

1. **疎通確認**: `python3 test_connection.py`を実行
2. **Claude Codeの使用**: `claude`コマンドでClaude Codeを使用

