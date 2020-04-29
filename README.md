# VSCode TypeScript 開発体験 ハンズオン

## ゴール

- Type Script の役割を理解し、VSCode で開発ができるようになること
- VSCode で Type Script でサーバアプリケーションをコンパイル、デバッグができる
- VSCode で Type Script で Web フロントエンドのアプリケーションをコンパイル、デバッグできる

## 解説すること

- Type Script とは何をするコンパイラであるか
- VSCode で Node.js 上で動作する Type Script の開発環境の構築方法、開発方法、デバッグ方法
- VSCode で Chrome 上で動作する Type Script の開発環境の構築方法、開発方法、デバッグ方法

## 解説しないこと

- Node.js 、 npm のインストール方法、及び使い方（コマンドで紹介します）
- Vue.js の使い方（完成品ソースコードを提供します）
- VSCode のインストール方法（[公式ドキュメント(英語)](https://code.visualstudio.com/docs/setup/setup-overview)、[KC さんの記事](https://employment.en-japan.com/engineerhub/entry/2019/06/21/103000)、もしくは書籍[Visual Studio Code 実践ガイド](https://gihyo.jp/book/2020/978-4-297-11201-1)を参照下さい）

## 準備が必要なもの

- Windows、もしくは MacOS の開発用 PC（Linux は Zoom が正常に動作しないため不可、クライアントは Windows/MacOS でリモート開発機能で Linxu の SSH 接続先環境を用意している、リモートコンテナ機能の使用は可）
- Windows の場合、[Git のインストール](https://gitforwindows.org/)
- [VS Code Meetup Slack への参加(こちらのページに案内リンクがあります)](https://vscode.connpass.com/)
- [Zoom クライアントのインストール](https://zoom.us/download)、及び音声、画面共有のテスト
- [Visual Studio Code のインストール]
- [Node.js のインストール](https://nodejs.org/ja/)
- [Chrome ブラウザのインストール](https://www.google.co.jp/chrome/)

### VSCode で準備が必要なもの

以下の拡張機能を、事前にインストールして下さい

- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)
  - 事前に、"Start collaboration session..." をクリックし、Microsoft アカウント、Github アカウントとリンクさせておいて下さい
- [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome)

## ご容赦いただきたいこと

- このハンズオンは有志の実験的取り組みです。至らない点など多数あるかと思いますが、参加者同士でコミュニケーションをとっていただき、一緒に解決できればと思います。
- Live Share を使ってのハンズオンなど、主催者としても初めての取り組みを行っています。ご不便をおかけする点も多いと思いますが、ご協力いただければと思います。
- Live Share は、Share の仕方を誤ると、ターミナルを横取りできたり、ターミナルやプログラムを介して、個人の機密情報にアクセスすることができうるプロダクトです。自己責任の上、注意して使用して下さい。また、もしアクセス可能だとしても他人の情報にはアクセスしないようにして下さい。
- このハンズオンの内容には、書籍[Visual Studio Code 実践ガイド](https://gihyo.jp/book/2020/978-4-297-11201-1)の内容が含まれます。資料は用意するため、購入は必須はありませんが、購入を検討いただければ幸いです。
- 本ハンズオンの内容を、de:code などカンファレンスで紹介することがあります。

## アジェンダ

1. Live Share 機能を使って、環境を公開してみよう
2. Type Script のプロジェクトをセットアップしよう
3. Type Script の Node.js アプリケーションをデバッグしよう
4. Type Script の Vue.js アプリケーションをセットアップしよう
5. フロントエンドとサーバサイドを同時にデバッグしよう

## コミュニケーションのとり方

- ハンズオン中は Zoom を繋ぎっぱなしにしてください。morimoto さんと呼んでいただければ、応答します！
- VSCode Meetup Slack にチャンネルを開設して、筆談が良い場合、
- Live Share を活用しましょう！ Live Share で "Start collaboration session..." をクリックすると、クリップボードに Live Share のリンクが作成されます。これを Slack に共有して下さい。Live Share で聞きに行きます！
