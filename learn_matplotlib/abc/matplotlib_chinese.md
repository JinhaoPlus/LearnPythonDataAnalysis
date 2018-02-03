# Matplotlib中文字体显示

## 在Mac上安装Matplotlib

不使用Anaconda，直接使用pip安装即可：

    pip3 install matplotlib



## 向Matplotlib添加中文字体`Microsoft YaHei(微软雅黑)`

Matplotlib不能默认使用中文字体显示字符的原因只是因为其未包含中文字体文件，所以导入中文字体文件到Matplotlib中即可。

Matplotlib的安装位置，如果使用`pip3`安装则其默认的安装路径在`/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/matplotlib/`。
当然你也可以通过如下程序确定你的Mac上的Matplotlab的安装路径：


```python
import matplotlib
print(matplotlib.matplotlib_fname())
```

打开这个目录可以看到这个路径下的`mpl-data/fonts/ttf/`，这个就是Matplotlib引入字体的路径，我们只需要把微软雅黑字体的ttf文件拷贝到其中即可。

## 修改Matplotlib的默认字体配置

仍然在上述的Matplotlib安装路径中，可以看到`mpl-data/matplotlibrc`这个文件，这个就是Matplotlib的配置文件。

在这个文件中搜索`font.family`，将`#`删除即把此行注释打开。则Matplotlib现在的默认字体族是：

```bash
font.family         : sans-serif
```
再在这个文件中搜索`font.sans-serif`，将`#`删除即把此行注释打开，然后在这个配置的最前面加上`Microsoft YaHei`：

```bash
font.sans-serif     : Microsoft YaHei, DejaVu Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
```
则`Matplotlib`现在的默认`sans-serif`字体族会最先使用`Microsoft YaHei`去展示字体，而这个`Microsoft YaHei`就可以展示中文字体了。

## 清除字体缓存

为了更好地看到效果，最好可以清楚之前Matplotlib生成的缓存文件，打开`~/.matplotlib`路径，其中可以看到`fontList.json`和`tex.cache`，前者其实就是字体列表的缓存文件，可以删除之：

```bash
rm -rf fontList.json
```

## 测试效果

如下测试代码查看是否生效：

```python
# coding:utf-8
import matplotlib.pyplot as plt

plt.plot((1, 2, 3), (4, 3, -1))
plt.xlabel(u'横坐标')
plt.ylabel(u'纵坐标')
plt.show()
```
执行效果如下所示：

![](https://ws4.sinaimg.cn/large/006tNc79ly1fo06rz2zdsj315s10479o.jpg)