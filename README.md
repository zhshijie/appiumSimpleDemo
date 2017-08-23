##  Appium-Desktop安装 
在[Appium-Desktop下载传送门](https://github.com/appium/appium-desktop/releases/tag/v1.2.0-beta.1)中下载最新版本的Appium-Desktop

### 必要的库安装，

如果没有安装过Homebrew,先安装[homebrew](https://brew.sh/)
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

如果没有安装npm,请移步 [node.js和npm安装](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143450141843488beddae2a1044cab5acb5125baf0882000)

安装依赖库
```
brew install libimobiledevice --HEAD
npm install -g ios-deploy  #如果是iOS10以上的系统才需要安装
```
如果没有安装 `libimobiledevice`，会导致Appium无法连接到iOS的设备，所以必须要安装，如果要在iOS10+的系统上使用appium，则需要安装`ios-deploy`


### appium-doctor 安装

```
npm install appium-doctor -g
```
安装后执行`appium-doctor --ios`指令，可以查看与iOS相关配置是否完整，下图是全部配置都成功,如果有那一项是打叉的，则进行安装就可以了。
```
appium-doctor --ios 
```
![Markdown](http://i1.bvimg.com/601834/30bc9c37a1ad13df.png)


### 更新Appium中的WebDriverAgent

1. 到[WebDriverAgent](https://github.com/facebook/WebDriverAgent)下载最新版本的WebDriverAgent
2. 进入下载后的`WebDriverAgent`文件
3. 执行 ./Scripts/bootstrap.sh
4. 直接用Xcode打开`WebDriverAgent.xcodepro`文件
5. 配置`WebDriverAgentLib`和`WebDriverAgentRunner`的证书 ![Markdown](http://i1.bvimg.com/601834/abc5109fa147c29b.png) ![Markdown](http://i1.bvimg.com/601834/1bd9a03466c080d3.png)
6. 连接并选择自己的iOS设备，然后按`Cmd+U`，或是点击`Product->Test`
7. 运行成功时，在Xcode控制台应该可以打印出一个Ip地址和端口号![Markdown](http://i1.bvimg.com/601834/39ae40b5a29f6f6b.png)
8. 在网址上输入`http://(iP地址):(端口号)/status`，如果网页显示了一些json格式的数据，说明运行成功。![Markdown](http://i1.bvimg.com/601834/deb83f6dff06df0d.png)
9. 进入到Appium中的WebDriverAgent目录，目录路径如下`(/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-xcuitest-driver/) `
10. 将自己下载并编译后的WebDriverAgent替换Appium原有的WebDriverAgent


### 运行Appium-Desktop

#### 准备工作

1. 需要一个.app 或是一个 .ipa 安装包，这个安装包是你要进行测试的应用程序
2. 测试应用程序对应的`bundleId`
3. 测试设备的`udid`,电脑连接上手机后，可以在Xcode的`Window->Deriver`中查看![Markdown](http://i1.bvimg.com/601834/33692992caee80e4.png)


#### 运行程序

1. 运行Appium-Desktop
2. 开启start server
3. 点击start new session 
4. 在 Desired Capabilities 中输入相关的[参数](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)后点击`Start Session`![Markdown](http://i1.bvimg.com/601834/911199f4359c3516.png)
5. 运行成功后，会弹出一个控制界面，在该界面中可以控制手机上正在运行的程序![Markdown](http://i1.bvimg.com/601834/c66f72da6d27ee1f.png)
6. 点击界面上方中心的录制按钮，可以将你对手机端的操作代码化![Markdown](http://i1.bvimg.com/601834/d764a92cad4e8e1d.png)


## 利用Appium-Python-Client进行iOS的自动化测试

### 准备工作
#### 安装python 
```
brew install python
```
#### 安装appium的python依赖库

```
git clone git@github.com:appium/python-client.git 
cd python-client
python setup.py install
```

#### 测试文件

在git上下载测试文件[appiumSimpleDemo](https://github.com/zhshijie/appiumSimpleDemo.git)
1. 一个简单的iOS工程文件
2. 一个简单的python测试文件




### 开始自动化测试

#### 配置iOS工程文件 

1. 打开下载后的`appiumSimpleDemo`文件，打开`appiumSimpleDemo.xcodepro`程序,配置下TARGET的签名![Markdown](http://i1.bvimg.com/601834/0b227bcf33ae3afc.png)
2. 在appiumSimpleDemo的根目录执行编译指令，编译出一个app文件`xcodebuild -sdk iphoneos -target appiumSimpleDemo -configuration Release`，编译成功后app文件的地址会打印在命令行中![Markdown](http://i1.bvimg.com/601834/c51c1f9f0906649f.png)
3. 将手机连接上电脑，在Xcode的`Window->Devices`中获取到设备的UDID![Markdown](http://i1.bvimg.com/601834/33692992caee80e4.png)

#### 配置python文件

打开`appiumSimpleDemo`中的`appiumSimpleDemo.py`文件,将，修改`setup`中的几个参数，将app的路径，设备的相关信息修改成当前连接设备的信息。![Markdown](http://i1.bvimg.com/601834/498483781b5b5a95.png),保存。




#### 运行Appium程序

打开之前下载安装的Appium，并开启服务。


#### 运行python测试文件

在`appiumSimpleDemo.py`所在的目录运行`python appiumSimpleDemo.py`，如果之前设置都没有出错，那么程序应该会在手机上成功运行，并自动点击了`entry next view`进入到了下一个界面，过了2s后会重新返回第一个界面


