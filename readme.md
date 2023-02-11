# Task

> 一个从终端创建便条, 并可设置优先级的小工具.

![效果图](https://github.com/wzk0/photo/blob/main/%E6%88%AA%E5%9B%BE%202023-02-11%2022-05-32.png?raw=true)

## 功能

1. 快捷地添加便条;
2. 为便条设置优先级;
3. 查看便条及信息(彩色);
4. 删除已有的便条.

## 安装

clone此仓库:

```sh
git clone https://github.com/wzk0/task
```

随后编辑`task.py`, 设置数据文件储存位置. 这步也可以跳过, 建议跳过使用默认的数据储存位置.

运行`setup.py`:

```sh
python3 setup.py
```

> 需要sudo权限.

完成安装后, 可直接使用`task`指令启动程序.

## 用法

```
usage(用法): task [-adhls] [thing ...]
example(例子):
  task -s 9 -a 'buy beef.'  --Add a note and set a 9 degree for it(添加一个便条并为它设置9级的优先度).
  task -d nbVJx  --Delete the note whose TID is nbVJx(删除一个TID为nbVJx的便条).

  ------- Listing options(参数详情) -------
  -a note(便条内容)			Add a note(新建一个便条).
  -d TID(TID)				Delete a note by TID(通过TID删除一个便条).
  -h					See the help(查看帮助).
  -l					List all your notes and informations(列出所有便条和相关信息).
  -s number(等级)			Set the degree you wanna give for the note(为一个便条设置优先级).
```