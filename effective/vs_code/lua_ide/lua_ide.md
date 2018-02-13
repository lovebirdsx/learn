# Modify Record

- luatool/ex/LuaIdeConfigManager.ts

``` TypeScript
// this.showIndex();
```

- lauch.json

``` Json
// "outDir": "${workspaceRoot}/out/src",
"outFiles": ["${workspaceRoot}/out/src/**/*.js"],
```

- luatool/ex/ExtensionManager.ts

``` TypeScript
// this.luaIdeConfigManager.showRecharge();
```

``` TypeScript
// this.barItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left);
// this.outPutChannel  = vscode.window.createOutputChannel("闲聊")
// this.outPutChannel.show(true)
// this.outPutChannel.appendLine("做着玩的一个小功能")
// context.subscriptions.push(this.barItem);
// context.subscriptions.push(this.outPutChannel);
// this.barItem.tooltip = "为了LuaIde 更好的发展,请支持LuaIde.";
// this.barItem.command = "luaide.donate";
// this.barItem.text = "捐献(LuaIde)";
// this.barItem.show();
```

- Extension.ts

``` TypeScript
function parseLuaFile(uri: vscode.Uri) {
	console.info(uri.toString());
	if(uri.fsPath.indexOf("FileTemplates") > -1 || uri.fsPath.indexOf("FunTemplate") > -1){
		return;
	}
	vscode.workspace.openTextDocument(uri).then(
		doc => {
			if (doc.languageId == 'lua') {
				luaParse.Parse(uri, doc.getText())
			}
		}
	)
}

vscode.workspace.findFiles("**/*.*", "", 10000).then(
	value => {
		value.forEach(element => {
			try {
				parseLuaFile(element);
			} catch (error) {

			}
		});
	})
```