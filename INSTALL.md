# Claude Code インストール手順

このドキュメントでは、Claude Codeのインストール手順を説明します。

## システム要件

- **Node.js**: 18以上（推奨: 20以上）
- **npm**: Node.jsとともにインストールされます
- **ネットワーク**: インターネット接続が必要

## インストール手順

### ステップ1: Node.jsのインストール

#### macOS（Homebrewを使用）.   

```bash
# Homebrewがインストールされていない場合
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Node.jsをインストール
brew install node
```

#### macOS（公式インストーラーを使用）

1. [Node.js公式サイト](https://nodejs.org/ja/)にアクセス
2. LTS（推奨）バージョンをダウンロード
3. インストーラーを実行してインストール

#### Linux

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Windows

1. [Node.js公式サイト](https://nodejs.org/ja/)からインストーラーをダウンロード
2. インストーラーを実行してインストール

### ステップ2: インストール確認

Node.jsとnpmが正しくインストールされたか確認します：

```bash
node --version
npm --version
```

期待される出力例：
```
v20.x.x
10.x.x
```

### ステップ3: Claude Codeのインストール

グローバルにClaude Codeをインストールします：

```bash
npm install -g @anthropic-ai/claude-code
```

インストールには数秒から数分かかる場合があります。

### ステップ4: インストール確認

インストールが成功したか確認します：

```bash
# コマンドが利用可能か確認
which claude

# バージョン確認
claude --version
```

## トラブルシューティング

### Node.jsが見つからない

**問題**: `node: command not found`

**解決方法**:
1. Node.jsがインストールされているか確認
2. パスが正しく設定されているか確認
3. ターミナルを再起動

### npmが見つからない

**問題**: `npm: command not found`

**解決方法**: Node.jsを再インストール（npmはNode.jsと一緒にインストールされます）

### Claude Codeコマンドが見つからない

**問題**: `claude: command not found`

**解決方法**:
1. インストールが完了したか確認
2. npmのグローバルパスを確認

```bash
# npmのグローバルパスを確認
npm config get prefix

# パスを環境変数に追加（必要に応じて）
export PATH="$(npm config get prefix)/bin:$PATH"
```

### 権限エラー

**問題**: `EACCES: permission denied`

**解決方法**: npmのグローバルディレクトリの所有者を変更

```bash
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

## 次のステップ

Claude Codeのインストールが完了したら、以下の手順に進んでください：

1. **Databricks側のセットアップ**: [DATABRICKS_SETUP.md](./DATABRICKS_SETUP.md)を参照
2. **設定ファイルの編集**: [SETTINGS.md](./SETTINGS.md)を参照
3. **疎通確認**: `python3 test_connection.py`を実行

