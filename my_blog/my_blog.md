# 1-django搭建个人博客

## 1-前言

​	django是一个由python写成的开源web应用框架，可以用它以更高的效率、更少的代码，搭建一个高性能的个人网站。

​	如果之前从未接触过web开发，并且快速上线自己的个性化网站，django绝对是你的最佳选择。

> 资源列表

本教程代码托管在GitHub：[Django_blog_tutorial](https://github.com/stacklens/django_blog_tutorial)

Django 的官方网站：[Django](https://www.djangoproject.com/)

撰写本文参考了以下资料，受益匪浅，并向读者强烈推荐：

- [跟老齐学Python：Django实战](https://www.itdiffer.com/)，书籍
- [追梦人物的博客](https://www.zmrenwu.com/)，网站
- [廖雪峰的官方网站](https://www.liaoxuefeng.com/)，网站

项目开发完毕后使用 Git/GitHub 分布式管理：[Windows环境下使用Git和GitHub](http://www.dusaiphoto.com/article/article-detail/13/)

> 遇到困难怎么办

- 认真检查代码拼写、缩进是否正确。
  - 一个标点符号的错误，可能会导致难以发现的问题
- 较简单的问题直接询问百度；若无法得到满意的答案请尝试Google以英文关键字搜索。要坚信全世界这么多学习django的人，你遇到的问题别人早就遇到过了。
- [Django官方网站](https://www.djangoproject.com/)是最权威的学习文档，英语不佳的同学，要有耐心仔细阅读
- 在本教程下留言，博主会尽量帮忙解决；也可以私信我：dusaiphoto@foxmail.com
- 实在无法处理的问题，可以暂时跳过。待到技术水平上升台阶，再回头来解决问题
- 若以上办法均不能解决你的问题，请在[StackOverflow](https://stackoverflow.com/)等技术网站上求助，那里有海量的热心程序员在等着你的问题

> 提问须知

​	













## 2-搭建开发环境

> 教程的开发环境

- win10（64位）
- python3.7.0
- django2.2

**注意：不少读者反馈 Django 2.1 版本在后面章节中会遇到 main.auth_user_old 的报错。这是版本兼容问题造成的。因此强烈建议读者使用其他小版本号，如 Django 2.2。**

> 安装python







> 配置虚拟环境









> 安装django







> 创建django项目

还是在虚拟环境下，在django_project文件夹中创建django项目：

```bash
(env) E:\django_project>django-admin startproject my_blog
```

查看`django_project`文件夹，发现多了`my_blog`文件夹，其结构应该是这样：

```bash
my_blog
│  db.sqlite3
│  manage.py
│
└─my_blog
    │  settings.py
    │  urls.py
    │  wsgi.py
    └─ __init__.py
```

这就是我们刚创建出来的项目了。

> 运行django服务器

django自带一个轻量的web开发服务器，也被叫做‘runserver’

- 开发服务器，是为了让你快速开发web程序，通过它可以避开配置生产环境的服务器的繁琐环节
- 开发服务器，会自动地检测代码的改变，并且自动加载它，因此在修改代码之后不需要手动去重启服务器，很方便

要运行这个django服务器，首先要进入my_blog文件夹，即含有manage.py文件的那个：

```
(env) E:\django_project>cd my_blog
(env) E:\django_project\my_blog>
```

输入命令`python manage.py runserver`：

```
(env) E:\django_project\my_blog>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 20, 2018 - 17:32:34
Django version 2.2, using settings 'my_blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

系统打印出这些信息，说明服务器启动成功了，打开chrome浏览器，输入http://127.0.0.1:8000/ ，即倒数第2排信息提示我们的服务器地址。看到下面的界面：

![img](D:\works\pactice\code_django\django_project\my_blog\图\hello_django_udoIHbf.jpg)



> 代码编辑器

​	django运行起来后，我们还需要一款**代码编辑器**或者**集成开发环境（IDE）**来编辑python文件，以达到开发需求。

市面上有很多Python的代码编辑器或者集成开发环境可以选择。

教程使用了代码编辑器**Sublime Text 3**。它不是免费的，但是可以无限期试用，所以你不需要掏腰包。

进入[Sublime Text 3官网](https://www.sublimetext.com/3)，下载对应版本的安装文件安装即可使用了。

当然你也可以根据喜好选择其他的编辑器或者开发环境：

- [10大Python集成开发环境和代码编辑器（指南）](https://blog.csdn.net/cH3RUF0tErmB3yH/article/details/80156176)
- [写python程序什么编辑器最好用？](https://www.zhihu.com/question/20476960)

> **浏览器**

作为一个正经的web开发者，你的眼中应该只有[Chrome](https://www.google.com/chrome/)！

> **总结**

经过以上一番折腾，总算是把趁手的工具都准备齐了。

准备好迎接正式的挑战吧。

- 有疑问请在[杜赛的个人网站](http://www.dusaiphoto.com/)留言，我会尽快回复。
- 或Email私信我：dusaiphoto@foxmail.com
- 项目完整代码：[Django_blog_tutorial](https://github.com/stacklens/django_blog_tutorial)

## 3-创建app

> 创建app

**在django中的一个app代表一个功能模块**

（开发者，可以将不同功能模块放在不同的app中，方便代码的复用）

（app就是项目的基石，因此开发博客的第一步就是创建新的app，用来是心啊跟文章相关的功能模块）

​	打开命令行，进入项目所在的目录：（虚拟环境下）

```
E:\>cd django_project
E:\django_project>
```

进入虚拟环境（忘记进入venv方法的看这里： [在Windows中搭建Django的开发环境](http://www.dusaiphoto.com/article/article-detail/4/)）：

```
 E:\django_project> env\Scripts\activate.bat
(env) E:\>
```

看到盘符前有`(env)`标识则表示进入虚拟环境成功。

输入`python manage.py startapp article`指令，创建名为`article`的app：

```
(env) E:\django_project\my_blog>python manage.py startapp article
```

查看一下`my_blog`文件夹，应该看到这样的结构：

```
my_blog
│  db.sqlite3
│  manage.py
│
├─article
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │
│  └─migrations
│        └─ __init__.py
│
└─my_blog
    │  settings.py
    │  urls.py
    │  wsgi.py
    └─ __init__.py
```

**项目结构分解如下**

- 根目录my_blog下有两个文件：
  - db.sqlite3是一个轻量级的数据库文件，用来存储项目产生的数据，比如博客文章；
  - manage.py是项目执行命令的入口，比如runserver
- 目录article是刚创建出来的app，用来放置博客文章相关的代码：
  - 后台管理文件admin.py
  - 数据模型文件model.py
  - 视图文件views.py
  - 存放数据迁移文件的目录migrations
- 根目录下，还有一个my_blog目录，其中的
  - settinzhag.py包含项目的配置参数，
  - urls.py是项目的跟路由文件

> 注册app（settings）

**接着需要修改项目配置文件，“告诉django现在有article这个一个app了”**

打开my_blog目录的settings.py，找到INSTALLED_APPS写入如下代码：

```python
my_blog/settings.py

INSTALLED_APPS = [
    # 其他代码
    ...

    # 新增'article'代码，激活app
    'article',
]
```

> 配置访问路径（urls）

**然后在给app配置访问路径url**

url可以理解为访问网站时，输入的网址链接，配置好url后，django才知道怎么定位app。

打开`my_blog`目录下的`urls.py`，增加以下代码：

```python
my_blog/urls.py

from django.contrib import admin
# 记得引入include
from django.urls import path, include

# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),

    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
]
```

path为django的路由语法：

- 参数article/分配了app的访问路径
- include将路径分发给下一步处理
- namespace可以保证反查到唯一的url，即使不同的app使用了相同的url（后面会用到）

记得在顶部引入`include`。

> 在开发环境下，article的url为：http://127.0.0.1:8000/article/

**还没结束**。现在我们已经通过`path`将根路径为`article`的访问都分发给article这个app去处理。但是app通常有多个页面地址，因此还需要app自己也有一个路由分发，也就是`article.urls`了。

> article可以有多个页面，如列表页面、详情页面等，那么就需要如下两个url：
>
> http://127.0.0.1:8000/article/list/
>
> http://127.0.0.1:8000/article/detail/
>
> app 中的 urls.py 就是用来区分它们的。

在app生成时并没有这个文件，因此需要自己在`article`文件夹中创建`urls.py`，在里面输入：

```
article/urls.py

# 引入path
from django.urls import path

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # 目前还没有urls
]
```

`urlpatterns`中暂时是空的，没写入任何路径的映射，不着急以后会写。

此时我们的app就配置完成了。

> 注意此时app还没有写好，因此启动服务器可能会报错，是正常的。
>
> Django2.0之后，app的`urls.py`必须配置`app_name`，否则会报错。

**总结**

本章创建了博客文章功能的app，学习了注册app并配置url。

下一章开始编写模型Model，理解Django的数据库处理。

- 有疑问请在[杜赛的个人网站](http://www.dusaiphoto.com/)留言，我会尽快回复。
- 或Email私信我：dusaiphoto@foxmail.com
- 项目完整代码：[Django_blog_tutorial](https://github.com/stacklens/django_blog_tutorial)

## 4-编写model模型

**django框架主要关注的是模型（model）、模板（template）和视图（views），称为MTV模式**

它们各自的职责如下：

| 层次                         | 职责                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| 模型（model），数据存取层    | 处理与数据相关的所有事务：如何存取、如何验证有效性、包含哪些行为以及数据之间的关系 |
| 模板（template），业务逻辑层 | 处理与表现相关的决定：如何在页面或其他类型文档中进行显示     |
| 视图（view），表现层         | 存取模型及调取恰当模板的相关逻辑。模型与模板的桥梁           |

**简单的来说，就是model存取数据，view决定需要调取哪些数据，而template则负责将调取的数据以合理的方式展现出来**

> 数据库与模型

​	数据库，是存储电子文件的场所，储存独立的数据集合。一个数据库由多个数据表构成。

```python
# 类比如下：
	三年级二班中同学们的花名册就是“数据表”
    有的花名册，记录每位同学的考试成绩、有的记录身高体重、还有的记录兴趣爱好
    所有的这些花名册都放到老师的柜子里，这个柜子就是“数据库”
```

​	操作书库使用的是复杂的sql语句，它是完全不同于python的另一种语言。

​	在django里写web应用并不需要你直接去操作数据库，而是定义好**模型**（用python语法），**模型**中包含了操作数据库所必要的命令。

（也就是说，你只需要定义数据模型，其他的底层代码都不用关心，它们会自动从模型生成）

```
	其实它由专门的术语，叫（对象关系映射，简称orm），用于实现面向对象编程语言里，不同类型系统的数据之间的转换。
```

> 编写mode.py

**如前面所讲，django中通过模型（model）映射到数据库，处理与数据相关的事务**

​	对于博客网站来说，最重要的数据就是文章。

​	所以首先，来建立一个存放文章的数据模型。

打开`article/models.py`文件，输入如下代码：

```python
article/models.py

from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
```

代码非常直白

- **每个模型都被表示为django.db.models.Model类的子类，从它继承了操作数据库需要的所有方法。**
- **每个字段都是Field类的实例。**比如：
  - 字符字段CharField
  - 日期时间字段DateTimeField.

(这将告诉django要处理的数据模型)

- **定义某些Field类实例需要参数。**比如：
  - CharField需要一个max_length参数。

（这个参数的用处，不仅是用来定义数据库结构，也用于验证数据）

- **使用ForeignKey定义了一个关系。**

（这将告诉django，每个（或多个） `ArticlePost` 对象都关联到一个 `User` 对象。）

```
Django具有一个简单的账号系统（User），满足一般网站的用户相关的基本功能。
```

`ArticlePost`类定义了一篇文章所必须具备的要素：作者、标题、正文、创建时间以及更新时间。

我们还可以额外再定义一些内容，规范`ArticlePost`中数据的行为：

```python
article/models.py

...

class ArticlePost(models.Model):
    ...

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
```

- 内部的Meta中ordering定义了数据的排列方式。
  - -created表示将以创建时间的倒叙排列，保证了最新的文章总是在网页的最上方

**（ordering是 元组，括号中只含一个元素时，末尾有逗号）**

- `__str__`方法定义了，需要表示数据时应该显示的名称。

（给模型增加`__str__`方法时很重要的，它最常见的就是在，django管理后台中作为对象的显示值。因此应该总是返回一个友好已读的字符串）

整理并去掉注释，全部代码放在一起是这样：

```python
article/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
```

> 导入

​	django框架基于python语言，而在python中用`import`或者`from---import`来导入模块。

​	**模块**其实就是一些函数和类的集合文件，它能实现一些相应的功能。

（当我们需要使用这些功能的时候，直接把相应的模块导入到我们的程序中就可以使用了）

​	`import`用于导入整个功能模块，（但实际使用时，往往只需要用模块中的某一个功能，为此导入整个模块有点大材小用）

​	因此可以用`from a import b`（表示从模块a总导入b给我用就可以了）

> 类

​	python作为面向对象编程语言，最重要的概念就是**类（class）和实例（instance）**

- **类**是抽象模板，而**实例**是根据这个类创建出来得到一个个具体的‘对象’。

（每个对象都拥有相同的方法，但各自的数据可能不同。而这些方法被打包封装到一起，就组成了类）

```python
# 例子如下：
	刚写的这个ArticlePost类，作用就是为博客文章的内容提供了一个模板。
    
    每当有一篇新文章生成的时候，都要对比ArticlePost类来创建author、title、body----等等数据
    虽然每篇文章的具体内容可能不一样，但是必须都遵循相同的规则。
```

​	在django中，数据由模型来处理，而处理模型的载体就是类（class）

> 字段

​	**字段（field）**表示数据库表的一个抽象类

（django使用字段类创建数据库表，并将python类型映射到数据库）

​	在模型中，**字段**被实例化为**类属性**并表示特定的**表**，同时具有将**字段**值映射到数据库的**属性及方法**。

```python
# 例子如下
	ArticlePost类中有一个title的属性，这个属性中保存着CharField类型的数据：即一个较短的字符串。
```

> 外键

​	数据库中有各种各样的数据表，有时候几张表的数据是互相关联的。

```python
# 例子如下：
	一张表，记录了所有的文章。
    另一张表，记录了所有的用户。
    
    （而文章是用户发表的）
    这时候，这两张表就产生了关系。
    
    外键--就是用来表示这个种关系的。
    
```

​	而`ForeignKey`是用来解决‘一对多’关系的，

```python
# 什么是‘一对多’？
	在ArticlePost模型中，
    一篇文章只能有一个作者，
    而一个作者，可以有很多篇文章
    
    这就是‘一对多’
```

​	因此，通过`ForeignKey`外键，将`User`和`ArticlePost`关联到了一起，最终就是将**博客文章的作者 和 网站的用户**关联在一起了。

​	既然有“一对多”，当然也有**“一对一”（`OneToOneField`）、“多对多”（`ManyToManyField`）**。目前用不到这些外键，后面再回头来对比其差别。

```
Django2.0 之前的版本外键的`on_delete`参数可以不填；

Django2.0以后`on_delete`是必填项。
```

> 内部类

​	内部类`class Meta`提供模型的元数据。元数据是“**任何不是字段的东西**”

```python
# 例如
	排序选项ordering
    数据库表名db_table
    单数 和 复数名称verbose_name 和 verbose_name_plural
    
   (这些信息不是某篇文章私有的数据，而是整张表的共同行为)
```

（要不要，写内部类是完全可选的，当然有了它可以帮助理解并规范类的行为。）

​	在`ArticlePost`中我们使用的元数据`ordering = ('-created',)`，表明了每当我需要取出文章列表，作为博客首页时，按照`-created`（即文章创建时间、符号表示倒序）来排列，保证了最新文章永远在最顶部位置。

> 数据迁移（migrations）

​	编写好model后，接下里就需要进行数据迁移。

（迁移，是django对模型所做的，更改传递到数据库种的方式）

**注意：每当对数据库进行了更改（添加、修改、删除等）操作，都需要进行数据迁移**

​	django的迁移代码，是由模型文件自动生成的，它本质上只是个历史记录，django可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的模型匹配。

在虚拟环境中进入`my_blog`文件夹（还没熟悉venv的再温习: [在Windows中搭建Django的开发环境](http://www.dusaiphoto.com/article/detail/4/)），输入`python manage.py makemigrations`，对模型的更改创建新的迁移表：

```
(env) e:\django_project\my_blog>python manage.py makemigrations
Migrations for 'article':
  article\migrations\0001_initial.py
    - Create model ArticlePost

(env) e:\django_project\my_blog>
```

通过运行 `makemigrations` 命令，Django 会检测你对模型文件的修改，并且把修改的部分储存为一次迁移。

然后输入`python manage.py migrate`，**应用迁移到数据库中**：

```
(env) e:\django_project\my_blog>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, article, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
  Applying sessions.0001_initial... OK

(env) e:\django_project\my_blog>
```

`migrate` 命令选中所有还没有执行过的迁移并应用在数据库上，也就是将模型的更改同步到数据库结构上。迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表。它专注于使数据库平滑升级而不会丢失数据。

**再重复一次**：每当你修改了`models.py`文件，都需要用`makemigrations`和`migrate`这两条指令迁移数据。

在迁移之后，Model的编写就算完成了。

**总结**

本章初步了解了Django的MTV模式，编写了博客文章的Model模型`ArticlePost`，并将其迁移到了数据库中。

## 5-初探view

​	数据库虽然已经有了，但是用户通常只需要这个很大的数据库中的很小一部分进行查看、修改等操作。

​	为此还需要代码，来恰当的取出并展示数据，这一部分代码就被成为“视图”

​	django中视图的概念是【一类具有相同功能 和 模块的网页的集合】。

```python
# 例子如下
	在一个博客应用中，你可能会创建如下几个视图：
```

- 博客首页：展示最近的几项内容
- 内容“详情”页：详细展示某项内容
- 评论处理器：用于响应为一项内容，添加评论的操作

这些需求都靠视图（view）来完成。

> hello world

​	首先写一个最简单的**视图函数**，在浏览器中打印出`Hello World!`字符串。

打开`article/views.py`，写出视图函数：

```python
article/views.py

# 导入 HttpResponse 模块
from django.http import HttpResponse

# 视图函数
def article_list(request):
    return HttpResponse("Hello World!")
```

**网页都是从视图派生而来**

​	每一个视图，表现为一个简单的python函数

他必须要做的只有两件事：

- 返回，一个包含被请求页面内容的HttpResponse对象
- 或者，抛出一个异常，比如Http404

（或者其他的）

​	视图函数中的`request`与网页发来的请求有关，里面包含get或post的内容、用户浏览器、系统等信息。

（django调用`article_list`函数时会返回一个含字符串的`httpresponse`对象）

​	有了视图函数，还需要配置URLconfs，将用户请求的URL链接关联起来（换句话说，URLconfs的作用时将URL映射到视图中）

[前面的文章](https://www.dusaiphoto.com/article/article-detail/6/)中已经将URL分发给了`article`应用，因此这里只需要修改之前添加的`article/urls.py`就可以。添加以下代码：

```python
article/urls.py

# 引入views.py
from . import views

...

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
]
```

**django将会根据，用户请求的url来选择使用哪个视图**

​	本例中当用户请求`article/article-list`链接时，会调用`views.py`中的`article_list`函数，并返回渲染后的对象。参数`name`用于反查url地址，相当于给url起了个名字，以后会用到。





> 准备工作

​	在章节编写model模型中，虽然定义了数据库表，但是这个表是空的，不方便展示view调取数据的效果。

(所以再写view之前，需要往数据表记录一些数据，接下里就是做这个工作)

> 网站后台概念

​	网站后台（网站管理后台）是指用于管理网站的一些列操作，如：数据的增删改查等。

​	在项目开发的储器，因为没有真是的用户数据和完整的测试环境，会频繁的使用后台修改测试数据。

​	Django内置了一个很好的后台管理工具，只需要些少量代码，就可以实现强大的功能。

> 创建管理员账号（superuser）

管理员账号（superuser）是可以进入网站后台，对数据进行维护的账号，具有很高的权限。

这里我们需要创建一个管理员账号，以便添加后续的测试数据。

**虚拟环境**中输入`python manage.py createsuperuser`指令，创建管理员账号：

```
(env) E:\django_project\my_blog>python manage.py createsuperuser
Username: dusai
Email address: dusaiphoto@foxmail.com
Password:
Password (again):
Superuser created successfully.
```

指令会提示你输入账号名字、邮箱和密码，根据喜好填入即可。

> 将ArticlePost注册到后台中

​	接下里需要“告诉”django，后台中需要添加ArticlePost这个数据表供管理。

打开`article/admin.py`，写入以下代码：

```
article/admin.py

from django.contrib import admin

# 别忘了导入ArticlerPost
from .models import ArticlePost

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
```

这样就简单的注册好了。













## 6-改写视图

上一章我们感受了视图的工作流程。

**为了让视图真正发挥作用，**改写`article/views.py`中的`article_list`视图函数：

```
article/views.py

from django.shortcuts import render

# 导入数据模型ArticlePost
from .models import ArticlePost

def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)
```

代码同样很直白，分析如下：

- `from .models import ArticlePost`从`models.py`中导入`ArticlePost`数据类
- `ArticlePost.objects.all()`是数据类的方法，可以获得所有的对象（即博客文章），并传递给`articles`变量
- `context`定义了需要传递给**模板**的上下文，这里即`articles`

> 模板的概念马上就要讲。

- 最后返回了`render`函数。它的作用是结合模板和上下文，并返回渲染后的HttpResponse对象。通俗的讲就是把context的内容，加载进模板，并通过浏览器呈现。

`render`的变量分解如下：

- request是固定的`request`对象，照着写就可以
- `article/list.html`定义了模板文件的位置、名称
- `context`定义了需要传入模板文件的上下文

视图函数这样就写好了。

> 编写模板（template）

在前面的视图中我们定义了模板的位置在`article/list.html`，因此在根目录下新建`templates`文件夹，再新建`article`文件夹，再新建`list.html`文件，即：

```
my_blog
│  ...
├─article
│  ...
└─my_blog
│  ...
└─templates
    └─ article
        └─ list.html
```

细心的你肯定注意到了，之前的Django文件后缀都是`.py`，代表Python文件；这里的模板文件后缀是`.html`，这又是什么呢？

**HTML是一种用于创建网页的标记语言。**它被用来结构化信息，标注哪些文字是标题、哪些文字是正文等（当然不仅仅这点功能）。也可以简单理解为“给数据排版”的文件，跟你写文档用的Office Word一样一样的 。

在`list.html`文件中写入：

```
templates/article/list.html

{% for article in articles %}
    <p>{{ article.title }}</p>
{% endfor %}
```

Django通过模板来动态生成HTML，其中就包含描述动态内容的一些特殊语法：

- **`{% for article in articles %}`：**
  - `articles`为视图函数的`context`传递过来的上下文，即所有文章的集合。
  - `{% for %}`循坏表示依次取出`articles`中的元素，命名为`article`，并分别执行接下来操作。
  - 末尾用`{% endfor %}`告诉Django循环结束的位置。
- **使用`.`符号来访问变量的属性。**
  - 这里的`article`为模型中的某一条文章；
  - 我们在前面的`ArticlePost`中定义了文章的标题叫`title`，因此这里可以用`article.title`来访问文章的标题。
- **`<p>...</p>`即为html语言，中间包裹了一个段落的文字。**

在上一章中已经定义好了`urls.py`，因此不再需要改动了。

一切都很好，深吸一口气。保存所有文件，在浏览器中输入地址`http://127.0.0.1:8000/article/article-list/`，得到以下错误：

![img](https://www.dusaiphoto.com/media/image/image_source/20180911/terror.jpg)

似乎成功从来都不会很顺利。

> 错误分析

虽然出错了，好在Django提供了非常完善的错误处理系统，方便开发者快速找到Bug的蛛丝马迹。

第一行就醒目地提示：**TemplateDoesNotExist**，说明Django没有找到`list.html`这个文件。仔细检查目录、文件的名称无误，没问题就往下继续看。

然后发现有这么两行：

```
...django\contrib\admin\templates\article\list.html (Source does not exist)
...django\contrib\auth\templates\article\list.html (Source does not exist)
```

似乎Django在这两个位置搜索（没有在刚创建的templates目录），没有发现需要的文件，然后返回了“未发现模板文件”的错误。

定位了问题的所在，接下来就是在如何“告诉”Django我的模板位置呢？

答案就在`settings.py`中了，它保存了Django项目的各种**初始配置**。

打开并找到这一段，加入代码`os.path.join(BASE_DIR, 'templates')`：

```
my_blog/settings.py

TEMPLATES = [
    {
        ...
        # 定义模板位置
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

这就是说模板文件在项目根目录的`templates`文件夹中，去找找吧。

保存文件，重新启动服务器：

![img](https://www.dusaiphoto.com/media/image/image_source/20180911/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE29.jpg)

成功！

虽然简陋，但是已经走通了MTV（model、template、view）环路。

不要激动，精彩的还在后面。

> 三个工具

​	开发中，会遇到各种各样的问题。

解决问题的方法很多，其中有三个工具非常的有效：

- **django报错页面**
  - 就是上面出现的那个黄黄的报错页面。
  - django报错页面，在大多数情况下，都能准备的判断错误类型、错误抛出的位置、甚至是解决方法。
- **浏览器控制台**
  - 如果你用的浏览器是Chrome，那么打开控制台的快捷键是`Ctrl + Shift + i`。
  - 控制台里又有两个子页面很常用：
    - **Elements**这里列出整个网页源码，可以在这里查看css样式的继承情况、容器的相互关系，甚至可以动态修改源码查看效果。
    - **Console**类似运行Django的命令行。如果浏览器运行网页时遇到故障（比如`404 未找到资源`、`403 服务器通讯失败`、`500 服务器内部错误`），都会在这里提示。

  - 以后还可以在JavaScript代码中用`console.log()`指令将感兴趣的内容打印到Console中查看。**非常非常有用**。

- print（）：
  - 在django中，在视图函数中写的print（）会打印到命令行中。












## 7-改写模板









## 8-文章详情

> 编写视图函数

- `article_detail(request, id)`函数中多了id这个参数。
  - （再写model的时候，没有写叫做id的字段）这时django自动生成的用于索引数据库的主键。
  - 有了它才有办法直到到底应该取出哪篇文章。
- `articlePost.objects.get(id=id)`
  - 意思是在所有文章中，取出id值相符合的唯一的一篇文章
- `<int:id>`:
  - Django2.0的`path`新语法用**尖括号<>**定义需要传递的参数
  - 这里需要传递名叫`id`的整数到视图函数中去

> 编写模板



> 优化网页入口

```html

            <!-- 改写了这里的 href --> 
            <a class="nav-link" href="{% url 'article:article_list' %}">文章</a>
```

- href定义了链接跳转的地址
- `{% url '---' %}`
  - 是django规定的模板解耦语法，用它可以根据我们在urls.py中设置的名字，反向解析到对应的url中去
- 关于其中的`'article:article_list'`的解释：
  - 前面的`article`是在项目根目录的`urls.py`中定义的app的名称
  - 后面的`article_list`是在app中的`urls.py`中定义的具体的路由地址

通过这样的方法就将链接跳转的指向给配置好了，只要对应url的名称不变，url本身无论怎么变化，Django都可以解析到正确的地址，很灵活。



**留意文章的id是如何传递的：**

- 在`list.html`中，通过`href="{% url 'article:article_detail' article.id %}"`，将id传递给`article/urls.py`
- 在`article/urls.py`中，通过`<int:id>`传递给视图函数`article_detail()`
- 在视图函数`article_detail()`中，通过形参`id`取得了文章的id值，并进行处理，最终定位了需要获取的文章对象

现在我们可以通过链接访问网站上的不同页面了，而不需要手动输入url。当然这也是现代网站的基础。







## 9-使用markdown

上一章我们实现了文章详情页面。为了让文章正文能够进行标题、加粗、引用、代码块等不同的排版（像在Office中那样！），我们将使用Markdown语法。

## 安装Markdown

**Markdown**是一种轻量级的标记语言，它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的或者HTML文档。建议读者一定要花五分钟时间熟悉一下Markdown的语法，熟练后码字效率一定会大幅提高。

关于Markdown语法看这里：[Markdown 语法介绍](https://coding.net/help/doc/project/markdown.html)

安装markdown也很简单：进入虚拟环境，输入指令`pip install markdown`即可。









## 10-发表新文章

前面我们已经学会如何用Markdown语法书写文章了。

但是还有问题呀。之前写文章都是在后台中进行的，**万一有别的普通用户也要发表文章怎么办？万一我想拓展些后台中没有的提交验证功能又怎么办？**

本章即讲述如何在前台中提交新的文章，以便满足开发者各种各样的*特殊需求*。

> Form表单

​	**在HTML中，表单是在 `<form>...</form>` 中的一些元素**，**它允许访客做类似输入文本、选择选项、操作对象或空间等动作，然后发送这些信息到服务端。**

​	一些表单界面元素（文本框或复选框）非常简单并内置在HTML中，而其他会复杂些：像弹出日期选择等操作控件。

​	处理表单很复杂。想想看Django的admin，许多不同类型的数据可能需要在一张表单中准备显示，渲染成HTML，使用方便的界面进行编辑，传到服务器，验证和清理数据，然后保存或跳过进行下一步处理。

​	django的表单功能的核心组件时form类，它能够描述一张表单并决定它如何工作及实现。

```

```

​	

1. 当视图函数接收到一个客户端的request请求时，首先根据request.method判断用户是要提交数据（post）还是获取数据（get）
2. 如果用户是要提交数据，将post给服务器的表达数据，赋于article_post_form实例。然后使用django内置方法.is_vaid()判断提交的数据是否满足模型的要求
3. 入股o



form实例可以绑定到数据，也可以不绑定数据

- 如果绑定到数据，就能验证该数据并将表单呈现为html并显示数据
- 如果它没有绑定数据，则无法进行验证（因为没有要验证的数据！），但仍然可以将空白表单呈现为HTML。

要将数据绑定到表单，就将数据作为字典作为第一个参数传递给Form类构造函数：



## 11-删除文章

> 不安全的方式

- 和查询文章类似，因为需要知道具体应该删除那一篇文章，因此必须传入文章的id
- 然后，调用.delete()函数删除数据库中的这篇问文章的条目
- 最后，删除成功后返回到文章列表

（这里，不对用户的身份进行限制，即任何人都可以删除任意文章。）

（当然这样肯定不是不符合常理的）

> 增加弹窗
>





> 安全的方式

​	可能你认为删除文章功能实现起来没什么难度，但是请注意，**上面的方法是有隐患的**。要继续深入探讨，就得提到**跨域请求伪造攻击**，也称为**CSRF攻击**了（Cross-site request forgery）。

> ​	CSRF攻击

CSRF攻击可以理解为：攻击者盗用了你的身份，以你的名义发送恶意请求

```python
# 例子如下：
1-用户登录了博客网站A，浏览器记录下这次会话，并保持了登陆状态
2-用户在没有退出登录的情况下，又非常不小心的打开了邪恶的攻击网站B
3-攻击网站B在页面中植入恶意代码，悄无声息的向博客A发送删除文章的请求，此时浏览器误以为时用户在操作，从而顺利的执行了删除操作。
```

​	**由于浏览器的同源策略，CSRF攻击者并不能得到你的登录数据实际内容，但是可以欺骗浏览器，让恶意请求附上正确的登录数据。**

​	不要小看CSRF攻击的威力：倘若是你的银行账户具有此类安全漏洞，黑客就可以神不知鬼不觉转走你的所有存款。

所以这里如何防范CSRF攻击的风险呢？方法是有的，即删除文章时用POST方法，并且校验`csrf`令牌。



> CSRF令牌

前面我们讲到在 Django 中提交表单必须加`csrf_token`，这个就是CSRF令牌了，它防范CSRF攻击的流程如下：

1. 当用户访问django站点的时候，django反馈给用户的表单中有一个隐含字段`csrf_token`，这个值是在服务器端随机生成的，每次都不一样
2. 在后端处理POST请求前，django会校验请求的cookie里面的csrf_token和表单里的csrf_token是否一致。一致则请求合法，否则这个请求可能是来自于 CSRF攻击，返回 403 服务器禁止访问。

**由于攻击者并不能得到用户的 cookie 内容（仅仅是靠浏览器转发），所以通常情况下是无法构造出正确的 `csrf_token` 的，从而防范了此类攻击。**

原理就是这样，下面来看看如何实现安全的删除功能。





## 12-修改文章

**实际上修改文章与新建文章有点类似**，不同的地方有两点：

- 修改是在原有文章的基础上，因此需要传递id指明具体需要修改的文章
- 加载页面时，需要将原来的内容作为默认值填写到表单中，因此需要将文章对象传递到html中

> 视图函数





更新的视图和创建文章非常相似，但又有点区别:

- 文章的id作为参数传递进来了
- 用户post提交表单时，没有创建新的文章，而是在之前的文章中修改
- redirect函数没有返回文章列表，而是返回到修改后的文章页面去了，因此需要同时把文章的id也打包传递进去，这时url所规定的
- get获取页面时将article对象也传递到模板中去，以便后续的使用









## 13-用户的登录和登出

用户数据时大部分网站最重要的资产。

**用户管理**就是对用户数据进行增删改查等操作的功能。

在django中用app来区别不同功能的模块，达到代码隔离和复用。因为用户管理和博客文章的共呢个不同，因此需要新建一个专门的app。

> 在遇表单类

用户登陆时，需要填写账户密码等表单数据，因此又要用到form表单类。

在前面发表文章的模块中，表单类继承了`forms.ModelForm`，这个父类**适合于需要直接与数据库交互的功能**，比如新建、更新数据库的字段等。如果表单将用于直接添加或编辑Django模型，则可以使用 `ModelForm`来避免重复书写字段描述。

而`forms.Form`则需要手动配置每个字段，**它适用于不与数据库进行直接交互的功能**。用户登录不需要对数据库进行任何改动，因此直接继承`forms.Form`就可以了。



- 与发表文章的表单类类似，form对象的主要任务就是验证数据
  - 调用is.valid()方法验证，并返回指定数据是否有效的布尔值
- form不仅负责验证数据，还可以“清洗”它。将其标准化为一致的格式。
  - 这个特性使得，它允许以各种方式输入特定字段字段的数据，并且始终产生一致的输出。
  - 一旦form使用数据创建了一个实例，并对其进行了验证，就可以通过cleaned_data属性访问清洗之后的数据
- authentic()方法验证用户名称和密码是否匹配
  - 如果是，则将这个用户数据返回
- login()方法实现用户登陆，将用户数据保存在session中



> 什么是session

session在网络应用中，称为“会话控制”，它存储特定用户会话所需的属性及配置信息。

当用户在web页之间跳转时，存储在session对象中的变量将不会丢失，而是在整个用户会话中一致存在下去

session最常见的用法就是，存储用户的登陆数据

> 

这里使用了新的模板语法：{% if ... %}，用来判断用户是否已经登录：

- 如果用户已经登录，则显示一个名字为用户名称的下拉框，就像通常的社交网站一样。
- 如果用户未登录，则显示“登录”两个字提醒用户可以点击登录。

`is_authenticated`是`models.User`类的属性，用于判断用户是否已通过身份验证。





## 14-用户的注册

> 注册表单类

用户注册是会用到**表单**类来提交账号、密码等数据，所以需要写注册用的表单/userprofile/forms.py

```

```

对数据库进行操作的表达那应该继承forms.ModelForm,可以自动生成模型中已有的字段。

这里我们覆写了pasword字段，一位通常在注册的时候需要重复输入password来确保用户没有将密码输入错误，所以覆写掉它以变我们自己i进行数据的验证工作。

def clean_password2()中的内容便是在验证密码是否一致了

def clean_[字段]这种写法django会自动调用，来对单个字段的数据进行验证清洗

**覆写某个字段之后，内部类class Meta中定义对这个字段就没有效果了，所以fields不用包含password**

**注意：**

- 验证密码一致性方法不能写`def clean_password()`，因为如果你不定义`def clean_password2()`方法，会导致password2中的数据被Django判定为无效数据从而清洗掉，从而`password2`属性不存在。最终导致两次密码输入始终会不一致，并且很难判断出错误原因。
- 从post中取值用的data.get('password')是一种稳妥的写法，即使用户没有输入密码也不会导致程序错误而跳出。前面章节提取post数据我们用来data['password']，这种取值方式如果不包含password，django会报错。另一种防止用户不输入就提交的方式是在表单中插入required属性。













## 15-用户的删除

> 权限与视图

用户数据是很多网站最重要的财产，**确保用户数据的安全是非常重要的**。

- 前面学习的用户登录、退出、创建都是相对安全的操作；
- 而删除数据就很危险，弄不好会造成不可逆的损失。
- 因此我们希望对操作者做一些限制，
  - 比如只能用户登录且必须是本用户才能进行删除的操作。这就是**权限**。

```

```

分析代码：

- `@login_required`是一个**Python装饰器**。
  - 装饰器可以在不改变某个函数内容被的前提下，给这个函数添加一些功能。
  - 具体来说就是`@login_required`要求调用`user_delete()`函数的时候，要求用户必须登陆；如果未登录则不执行函数，将页面重定向到`/userprofile/login/`地址去。
- 装饰器确认用户已经登陆后，允许调用`user_delete()`；
  - 然后需要删除的用户id通过请求传递到视图中，由if语句确认是否与登陆的用户一致，成功后则退出登陆并删除用户数据，返回博客列表页面



- 因为删除用户要求用户必须登陆，因此就把它的入口放在登陆后才显示的下拉框中，这样页面可以更加简洁。当然这种方式并不是最佳的选择，通常的做法是把删除功能放在独立的用户资料页面中。
- 与删除文章类似，点击删除用户链接后调用了`user_delete()`函数，函数包含了



## 16-重置用户密码

前面我们已经知道如何修改文章标题、正文等内容，但是密码作为验证身份的重要口令，必须以更加稳妥的方式修改。

​	一种比较常用的方式是**发送一封修改密码的邮件,到用户事先绑定的邮箱里**。

业务流程分析如下：

- 向用户邮箱发送包含重置密码地址的邮件。邮件的地址需要动态生成，防止不怀好意的用户从中捣乱；
- 向网站用户展示一条发送邮件成功的信息
- 用户点击邮箱中的地址后，转入重置密码的页面
- 向用户展示一条重置成功的信息

上面4个步骤包含了4个视图和模板，自己写代码看来有些繁琐。

可能你会想，Django这种以开发效率著称的框架，**重置密码这种常用功能是不是内置了呢**？答案是肯定的。事实上内置模块的流程和上面的是完全相同的，你只需要将上面4个步骤的`url`配置好就可以使用了。当然内置的模板很简陋，你可以覆写模板变成自己网站的风格。

```
实际上Django不仅内置了密码重置，还包括登录、登出、密码修改等功能。建议读者到一定水平后多阅读Django的源码，学习其中的编程技巧。另外这部分内容Django是用**类视图**写的，现在阅读可能有一定困难。

源码位置：/env/Lib/site-packages/django/contrib/auth/views.py

官方文档：[Django 的验证系统https://docs.djangoproject.com/zh-hans/2.1/topics/auth/default/)
```





## 17-扩展用户信息

Django自带的User模型非常实用，以至于我们没有写用户管理相关的任何模型。

**但是自带的User毕竟可用的字段较少。比方说非常重要的电话号码、头像等都没有。解决的方法有很多，你可以不使用User，自己从零写用户模型；也可以对User模型进行扩展。**



每个profile模型对应唯一的一个user模型，形成了对user的外界扩展，因此你可以在profile添加任何想要的字段。

（这种方法的好处时不需要对user进行任何改动，从而拥有完全自定义的数据表。型本身没有什么新的知识，比较神奇的是用到的**信号机制**。）

**Django包含一个“信号调度程序”，它可以在框架中的某些位置发生操作时，通知其他应用程序。--------------------------简而言之，信号允许某些发送者通知一组接收器已经发生了某个动作。当许多代码可能对同一事件感兴趣时，信号就特别有用。**

这里引入的`post_save`就是一个内置信号，它可以在模型调用`save()`方法后发出信号。

有了信号之后还需要定义接收器，告诉Django应该把信号发给谁。装饰器`receiver`就起到接收器的作用。每当`User`有更新时，就发送一个信号启动`post_save`相关的函数。

通过信号的传递，实现了每当`User`创建/更新时，`Profile`也会自动的创建/更新。



> 重建数据库

前面讲过，每次改动模型后都需要进行数据的迁移。由于`avatar`字段为图像字段，需要安装第三方库`Pillow`来支持：



> 配置admin





## 18-上传用户头像

上一章中预留了avatar字段，用来保存用户上传的头像，现在我们来实现这个功能。

> 必要的设置

图片属于一种媒体文件，它与静态u文件类似，需要设置一个统一的目录，便于集中存储和访问。

**MEDIA_ROOT**和**MEDIA_URL**是用户上传文件保存、访问的位置：

- 前面的profile中我们设置了upload_to参数。
  - 有了这个参数，文件上传后将自动保存到项目根目录的media文件夹中。os.path.join(MEDIA_ROOT, 'media/')指定了media文件夹的位置
- MEDIA_URL代表用户通过URL来访问则会个本地地址的URL。
  - 设置好这个参数后，用户就可以通过解析url，很方便的获取文件的地址。这样做的好处是比米娜的硬编码，让代码更容易维护

Django框架擅长的是对逻辑的处理，而对图片这类文件的处理则非常的耗时。因此在实际的**生产环境**中（即产品上线之后），通常是有专门的Web服务器来处理文件的访问。



> 编写mtv

`upload_to`指定了图片上传的位置，即`/media/avatar/%Y%m%d/`。`%Y%m%d`是日期格式化的写法，会最终格式化为系统时间。比如说图片上传是2018年12月5日，则图片会保存在`/media/avatar/2018205/`中。

```
注意ImageField字段不会存储图片本身，而仅仅保存图片的地址。

记得用pip指令安装Pillow。
```



- 表单上传的文件对象存储在类字典对象request.FILES中，
  - 因此需要修改表单类的参数，将它一并传递进去。
- 如果`request.FILES`中存在键为`avatar`的元素，则将其赋值给`profile.avatar`（注意保存的是图片地址）；否则不进行处理。



- 模板语法`{% if ... %}`判断用户是否上传头像。
- `<img>`标签用于显示图片内容；在`style`属性中规定了图片的最大宽度并带有一点的圆角。
- **注意**，表单必须设置`enctype="multipart/form-data"`属性，才能够正确上传图片等文件。
- 添加`<input type="file" ...>`标签用于上传图片。



## 19-文章分页

随着时间的推移（**加上勤奋的写作！**），你的博客文章一定会越来越多。如果不进行处理，可能同一个页面会挤上成百上千的文章，不美观不说，还降低了页面的反应速度。

这个时候就需要对文章进行分页的处理。

> 利用轮子

写一个完善的分页功能是有些难度的，好在Django已经帮你准备好一个现成的分页模块了（Django把大部分基础功能都替你准备好了！）。内置模块虽然简单，但是对博客来说完全足够了。

我们要用到的是`Paginator`类。在`Shell`中可以充分尝试它的用法：



```

```

在视图中通过paginator类，修改模板返回的内容：

- 返回的不再是所有文章的集合，
- 而是对应页码的部分文章的对象，并且这个对象还包含了分页的方法



我们在前面的文章已经接触过一些将参数传递到视图的手段了：

- 通过post请求，将表单数据，传递到视图
- 通过url，将地址中的参数，传递到视图

**这里还用到了另一种方法：在GET请求中，在url的末尾附上`？key=value`的键值对，视图中就可以通过`request.GET.get('key')`来查询`value`的值**











## 20-文章浏览量

**文章浏览量**是所有社交类网站所必备的数据，足以显示其重要性了。

博主可以通过浏览量来评估某篇文章的受欢迎程度，读者也能够通过浏览量来筛选质量更高的文章。

然而，准确统计浏览量并不简单：

- 某些类型的请求不应该统计为浏览量，比如作者自己的浏览或编辑文章之后的重定向请求
- 由于用户众多，浏览量的数据时刻都在快速更新，会给数据库带来很大的压力。因此很多大型网站都会使用如[Redis](https://redis.io/)这样的读写速度非常快的内存数据库辅助存储。

> 模型

浏览量作为每篇博文都有的数据，需要一个字段来存储。

因此修改文章的模型：

```

```

- `PositiveIntegerField`是用于存储正整数的字段
- `default=0`设定初始值从0开始



> 详情模板

除了文章列表外，通常详情页面中也需要显示浏览量。

除此之外，在前面的学习中为了方便，没有做任何**权限管理**，以至于任何用户都可以对所有文章进行修改、删除：

```

```

这样是肯定不行的，必须修复这个严重的错误。



修改内容有：

- 确认当前登录用户是文章的作者，才显示“删除文章、“编辑文章”两个链接
- 显示浏览量



> 视图

现在浏览量能够正确显示了，但是由于没有进行任何处理，其数值会一直为0。我们希望每当用户访问详情页面时，浏览量就加1。





## 21-最热文章

有了浏览量之后，文章受欢迎的程度就有了评价标准。随之而来的就有根据浏览量对文章进行排序的需求，即显示**“最热文章”**。

现在你已经很熟悉MTV模式，不需要我啰嗦也能完成任务：

- 文章的模型已经有了，不需要写Model了
- 写一个视图函数`article_list_by_views()`，取出按浏览排序后的文章对象
- 将文章对象传递到模板，并进行渲染

**很简单，但也隐藏着问题**：最热文章列表和之前的普通文章列表相比，大部分功能其实都是相同的，仅仅是排序不同而已。

万一哪天需要根据文章标题排序呢？万一还需要用户id排序、标签排序、收藏排序...不仅如此，就连路由`urls.py`都要跟着膨胀。代码会越来越臃肿且不可维护。

**重复的代码是万恶之源。**因此这里挑战一下，不创建新的视图/路由，而是将排序功能融合到已有的视图/路由中。



**重点如下**：

- 前面用过GET请求传递单个参数。它也是可以传递多个参数的，如`?a=1&b=2`，参数间用`&`隔开
- 视图根据GET参数`order`的值，判断取出的文章如何排序
- `order_by()`方法指定对象如何进行排序。模型中有`total_views`这个整数字段，因此‘total_views’为正序，‘-total_views’为逆序
- 为什么把新变量`order`也传递到模板中？因为文章需要翻页！`order`给模板一个标识，提醒模板下一页应该如何排序



## 22-搜索文章

不管是最新文章列表也好、最热文章列表也罢，都是把**所有**的文章数据全部展示给了用户。

但是如果用户只关心某些**特定类型**的文章，抽取全部数据就显得既不方便、又不效率了。

因此，给用户提供一个**搜索功能**，提供给用户感兴趣的几篇文章，就大有用处了。

### 准备工作

### 逻辑

​		尽管细节不同，但是**搜索和列表**有很多类似的地方：它们都是先检索出一些文章对象，并将其展示给用户。上一章已经说过，**代码重复是万恶之源**，好的实践必须把功能类似的模块尽量复用起来。基于这个原则，我们打算继续在原有的`article_list()`上添砖加瓦，让其功能更加的强大。

*随着项目越来越庞大，又需要将功能复杂的模块拆分成更简单的多个模块。目前我们还不用担心这个问题。*

**更酷的是，我们希望搜索出来的文章也能够按照时间、热度等各种方式进行排序。因此需要构造一个新的参数`search`，能够和之前的`order`参数进行联合查询。**

### GET还是POST？

用户搜索内容时提交的文本，可以用GET请求提交，也可以用POST请求提交。根据实际的需要进行选择。

因为`order`是用GET提交的，并且翻页是GET请求，因此选择GET方式提交搜索文本，可以方便地和之前的模块结合起来。

之前我们已经用过表单组件`<form method="POST">`，通过POST请求提交数据。表单组件同样也可以提交GET请求，只要去掉`method="POST"`属性就可以了。

### Q对象

`Model.objects.all()`能够返回表中的所有对象。

对应的，`Model.objects.filter(**kwargs)`可以返回与给定参数匹配的部分对象。

> 还有`Model.objects.exclude(**kwargs)`返回与给定参数不匹配的对象

如果想对多个参数进行查询怎么办？比如同时查询文章标题和正文内容。这时候就需要**Q对象**。



重点知识如下：

- 新增参数search，存放需要搜索的文本。
  - 如果search不为空，则检测特定文章对象
- 留意**filter**中**Q对象**的用法。
  - `Q(title__icontains=search)`意思是在模型的`title`字段查询，`icontains`是**不区分大小写的包含**，中间用两个下划线隔开。
  - `search`是需要查询的文本。多个Q对象用管道符`|`隔开，就达到了联合查询的目的。
  - *icontains不区分大小写，对应的contains区分大小写*
- 什么需要`search = ''`语句？
  - 如果用户没有搜索操作，则`search = request.GET.get('search')`会使得`search = None`，而这个值传递到模板中会错误地转换成`"None"`**字符串**！等同于用户在搜索“None”关键字，这明显是错误的。



```

```

- 面包屑组件、页码组件都改动了href：增加了`search`参数
- 新增搜索栏，以GET请求提交`search`参数；`required`属性阻止用户提交空白文本
- 新增搜索提示语。好的UI必须让用户了解当前的状态







## 23-文章目录

对会读书的人来说，读一本书要做的第一件事，就是仔细阅读这本书的目录。阅读目录可以对整体内容有所了解，并清楚地知道感兴趣的部分在哪里，提高阅读质量。

博文也是同样的，好的目录对博主和读者都很有帮助。更进一步的是，还可以在目录中设置锚点，点击标题就立即前往该处，非常的方便。

### 文中的目录

- 重新布局，将原有内容装进`col-0`的容器中，将右侧`col-3`的空间目录
- `toc`需要`|safe`标签才能正确渲染



## 24-发表评论

*有的人觉得奇怪，没有博文就没有评论，为什么说评论是“独立”的功能？*

​		*那是因为不仅博文可以评论，照片、视频甚至网站本身都可以“被评论”。将其封装成单独的模块方便以后的扩展。*

```python
class Comment(models.Model):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
```

有两个外键：

- article是被评论的文章
- user是评论的发布者





**因为模型中的2个外键将通过视图逻辑自动填写，所以这里只需要提交body就足够了**



- 表单组件中的`action`指定数据提交到那个url中
- 显示评论中`comments.count`是模板对象那个中内置的方法，对包含的元素进行计数
- `|date:"Y-m-d H:i :s"`：管道符你已经很熟悉了，用于给对象“粘贴”某些属性或功能。这里用于格式化日期的显示方式。请尝试修改其中的某些字符试试效果。

- `<pre>`定义预格式化的文本，在我们的项目中最关键的作用是保留空格和换行符。该标签会改变文字的字体、大小等，因此用`style`属性重新定义相关内容。尝试将`<pre>`替换为`div`，输入多行文本试试效果。



## 25-课间休息









## 26-类的视图

### 什么是类视图

前面章节中写的所有视图都是基于函数的，即`def`；而类视图是基于类的，即`class`。

**类**是面向对象技术中非常重要的概念。具有复杂**数据**、**功能**的类，可以通过继承轻而易举的将自身特性传递给另一个类，从而实现代码的高效复用。

**相比以前的函数视图，类视图有以下优势：**

- http方法（get、post等）相关的代码，可以通过**方法**而不是**条件分支**来组织
- 可以通过诸如mixins（多重继承）之类的面向对象技术将代码分解为**可重用组件**

### 列表

### 函数和类

假设我们有一个[博客列表](https://www.dusaiphoto.com/article/detail/16/)，列表有一个GET方法，那么用视图函数看起来像这样：

```python
def article_list_example(request):
    """处理get请求"""
    if request.method == 'GET':
        articles = ArticlePost.objects.all()
        context = {
            'articles': articles
        }
        return render(request, 'articles/list.html',context)
```

而在类试图中：

```python
from django.views import View

class ArticleListView(View):
    """处理get请求"""
	def get(self, request):
        articles = ArticlePost.objects.all()
        context = {
            'articles': articles
        }
        return render(request, 'article/list.html', context)
```

从本质上讲，基于类的视图允许你使用不同的**类实例方法**（即上面的`def get()`）响应不同的HTTP请求方法，而不需要使用**条件分支**代码。这样做的好处是把不同的HTTP请求都分离到独立的函数中，逻辑更加清晰，并且方便复用。

**需要注意的是**，因为Django的URL解析器希望将请求发送到**函数**而不是类，所以类视图有一个 `as_view()`方法，该方法返回一个函数，当请求匹配关联模式的URL时，则调用该函数。

即，视图函数的url原本写为：

```python
urlpatterns = [
    path('---/', views.article_list.as_view(), name='---')
]
```

### 通用视图

像**列表**这样的功能在web开发中是很常见的，开发者会一遍又一遍写几乎相同的列表逻辑。Django的**通用视图**正是为缓解这种痛苦而开发的。它们对常用模式进行抽象，以便你快速编写公共视图，而无需编写太多代码。

因此用列表通用视图改写如下：

```python
from django.views.generic import ListView

class ArticleListView(ListView):
    """
    上下文的名称
    查询集
    模板位置
    """
    context_object_name = 'articles'
    queryset = ArticlePost.objects.all()
    template_name = 'article/list.html'
```

列表继承了父类`ListView`，也就获得了父类中的处理列表的方法，因此你可以看到，我们在自己的类中没有写任何处理的逻辑，仅仅是赋值了几个变量而已。

### 动态过滤

从数据库中筛选特定的内容也是常见的需求，类视图如何实现呢？

你可能想到了，将上面代码中改为`queryset = ArticlePost.objects.filter()`就可以了。

除此之外，**更好的办法**是覆写`get_queryset()`方法：

```python
class ArticleListView(ListView):
    context_object_name = 'articles'
    template_name = 'article/list.html'
   
	def get_queryset(self):
        """
        查询集
        """
        queryset = ArticlePost.objects.filter(title='Python')
        return queryset
```

### 添加上下文

在博客列表的设计时，我们返回给模板的**上下文**除了`articles`以外，还有很多额外的信息，如`order`、`search`；在类视图中同样可以实现，改写`get_context_data()`方法即可：

```python
class ArticleListView(ListView):
    
    def get_context_data(self, **kwargs):
        """
        获取原有的上下文
        增加上下文
        """
        context = super().get_context_data(**kwargs)
        context['order'] = 'total_views'
        return context
```

除此之外，`ListView`还有些别的方法可以覆写，深入了解可以看这里：[官方文档](https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/generic-display/#listview)

### 混入类

**混入类（Mixin）**是指**具有某些功能、通常不独立使用、提供给其他类继承功能**的类。嗯，就是“混入”的字面意思。

前面的列表视图中已经有`get_context_data()`方法了。假设需要写一个功能类似的视频列表，就可以用**Mixin**来避免重复代码：

```python
views.py

...

class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = 'total_views'
        return context

class ArticleListView(ContextMixin, ListView):
    ...

class VideoListView(ContextMixin, ListView):
    ...
```

通过混入，两个子类都获得了`get_context_data()`方法。

*从语法上看，混入是通过多重继承实现的。有区别的是，Mixin是***作为功能***添加到子类中的，而不是作为父类。*

### 详情页

既然列表都有通用视图，详情页当然也有对应的`DetailView`。

用类视图写一个[简单的详情页](https://www.dusaiphoto.com/article/detail/19/)：

```python
from django.views.generic import DetailView

class ArticleDetailView(DetailView):
    queryset = ArticlePost.objects.all()
    context_object_name = 'article'
    template_name = 'article/detail.html'
```

url:

```python
urlpatterns = [
    path('detail_view/<int:pk>',views.ArticleDetailView.as_view(), name='---')
]
```

注意这里传入的参数不是`id`而是`pk`，这是视图的要求（也可以传入`slug`）。`pk`是数据表的主键，在默认情况下其实就是`id`。

这就写好了！

也可以添加任何别的功能，比如[统计浏览量](https://www.dusaiphoto.com/article/detail/45/)：

```python
class ArticleDetailView(DetailView):
    
    def get_object(self):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        # 浏览量+1
        obj = super(ArticleDetailView, self).get_obejct()
        obj.total_views += 1
        obj.save(update_fields=['total_views'])
        return obj
```

方法`get_object()`的作用是获取需要展示的对象。首先调用父类方法，将这个对象赋值给`obj`变量，然后再对其进行统计浏览量的操作，最后将对象返回。相当于在原有的方法中把自己的逻辑“塞”了进去。

关于`DetailView`更多特性看这里：[官方文档](https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/generic-display/#detailview)

### 编辑

除了能够展示信息，通用视图还包含`CreateView`、`UpdateView`、`DeleteView`等**编辑**数据的类。

如果要[新建文章](https://www.dusaiphoto.com/article/detail/22/)，则视图可以这么写：

```python
from django.views.generic.edit import CreateView

class ArticleCreateView(CreateView):
    model = ArticlePost
    
    fields = '__all__'
    # 或者只填写部分字段，比如：
    # fields = ['title', 'content']

    template_name = 'article/create_by_class_view.html'
```

创建`create_by_class_view.html`文件（目录在哪，你应该已经很清楚了），写入：

```html
create_by_class_view.html

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```

最后添加url：

```python
urls.py

urlpatterns = [
    path('create-view/', views.ArticleCreateView.as_view(), name='...'),
]
```

虽然外观简陋（这不是重点），但现在这个视图确实已经能够创建新文章了！

`UpdateView`和`DeleteView`这里就不再赘述了，以后用到的地方再进行讲解。

想提前了解的同学戳这里：[官方文档](https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/generic-editing/)



## 27-文章栏目

博客的文章类型通常不止一种：有时候你会写高深莫测的技术文章，有时候又纯粹只记录一下当天的心情。

因此**对文章的分类**就显得相当的重要了，既方便博主对文章进行分类归档，也方便用户有针对性的阅读。

而文章分类一个重要的途径就是设置**栏目**。

### 栏目的模型

实现文章栏目功能的方法有多种。你可以只是简单的在文章的Model中增加`CharField()`字段，以字符串的形式将栏目名称保存起来（实际上这种实现更像是**“标签”**，以后会讲到）。这样做的优点是比较简单；缺点也很明显，就是时间长了你可能会记混栏目的名字，并且也不方便对栏目的其他属性进行扩展。

因此对文章栏目可以独立为一个Model，用外键与文章的Model关联起来。

修改`article/modles.py`文件：

**实在不知道如何去实现的同学，请查看[教程代码](https://github.com/stacklens/django_blog_tutorial)文章列表的视图和模板，答案就在里面。**

## 28-文章标签

**“标签”**是作者从文章中提取的**核心词汇**，其他用户可以通过标签快速了解文章的关注点。每一篇文章的标签可能都不一样，并且还可能拥有多个标签，这是与栏目功能不同的。

好在标签功能也有优秀的三方库：[Django-taggit](https://github.com/jazzband/django-taggit)，省得自己动手设计了。快速开发就是这样，能“借用”就不要自己重复劳动。

### 安装及设置

首先在**虚拟环境**中安装Django-taggit：

```
pip install django-taggit
```

安装成功后，修改项目设置以添加库：

```
my_blog/settings.py

...
INSTALLED_APPS = [
    ...
    'taggit',
]
...
```



**需要注意的是，如果提交的表单使用了`commit=False`选项，则必须调用`save_m2m()`才能正确的保存标签，就像普通的多对多关系一样。**





注意Django-taggit中**标签过滤**的写法：`filter(tags__name__in=[tag])`，意思是在`tags`字段中过滤`name`为`tag`的数据条目。赋值的字符串`tag`用方括号包起来。

之所以这样写是因为Django-taggit还支持多标签的联合查询，比如：

```
Model.objects.filter(tags__name__in=["tag1", "tag2"])
```



## 29-文章标题图







## 30-富文本编辑器









## 31-四个小功能









## 32-多级评论



















## 34-消息通知

本篇将以`django-notifications`为基础，非常高效的搭建一个简易的通知系统。







## 35-描点定位









## 36-第三方登录

本章会介绍一个强大的库：`Django-allauth`，它不仅包含一整套的本地注册、登录、管理的解决方案，还支持GitHub、Twitter、微博、微信甚至百度等几十种第三方登录方式







## 37-自动化测试









## 38-日志记录

日志是指程序在运行过程中，对状态、时间、错误等的记录。即把运行过程中产生的信息输出或保存起来，供开发者查阅。

Django使用Python内置的`logging`模块处理日志。关于该模块的使用，[Python文档](https://docs.python.org/3/howto/logging.html)里有非常详细的讨论。如果你从未用过，本文提供一个快速入门。

日志事件的信息流程如下：

![img](D:\learning\面试\图\logging_flow.jpg)

一份日志配置由`Loggers`、`Handlers`、`Filters`、`Formatters`四部分组成。

### Loggers（记录器，入口）

**logger是记录器，是日志系统的入口，它有三个重要的工作：**

- 向应用程序（也就是你的程序）公开几种方法，以便运行时记录信息
- 根据传递给logger的消息的严重性，确定出需要处理的消息
- 将需要处理的消息传递给所有感兴趣的处理器（handler）

每一条写入logger的消息，都是一条日志记录。每一条日志记录也包含级别，代表对应消息的严重程序，**常用的级别如下：**

- debug：排查故障的时候，使用低级别系统信息，通常开发时使用
- info：一般的系统信息，并不算问题
- warning：描述系统发生的小问题的信息，但通常不影响功能
- error：描述系统发生的大问题的信息，可能会导致功能不正常
- critical：描述系统发生严重问题的信息，应用程序由崩溃风险

当logger处理一条信息时，会将自己的日志级别和这条信息的日志级别做对比。如果消息的级别匹配或高于logger的日志级别，它就会被进一步处理；否则这条信息就会被忽略掉

当logger确定了一条消息需要处理之后，会把它传给handler

### handlers（处理器）

**handler是处理器，它的主要功能是决定如何处理logger中每一条消息，比如把消息输出到屏幕、文件或者email中。**

和logger一样，handler也有级别的概念。如果一条日志记录的级别不匹配或者低于handler的日志级别，则会被handler忽略。

一个logger可以有多个handler，每一个handler可以有不同的日志级别。这样就可以根据消息的重要性不同，来提供不同类型的输出。例如：你可以添加一个handler把error和critical消息发到你的email，在添加一个handler把所有的消息（error和critical消息）保存到文件里。

### filters（过滤器）

**filter是过滤器。在日志记录从logger传到handler的过程中，使用filter来做额外的控制。例如只允许某个特定来源的error消息输出。**

filter还被用来在日志输出之前，对日志记录做修改。例如当满足一定条件时，把日志从error降到warning级别。

filter还logger和handler中都可以添加；多个filter可以链接起来使用，来做多重过滤操作。

### formatters（格式化器）

formatters时格式化器，主要功能是确定最终输出的形式和内容。

```python
my_blog/settings.py

...
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

- version：配置的版本
- disable_existing_loggers：是否禁止默认配置的记录器

（这两项通常不需要改动）

- 一条消息首先传递给logger。
  - django中内置了几种记录器，比如这里用到的django记录器，它会接收django层次结构中的所有消息
  - 然后我们定义了需要处理的debug以上级别的消息，并把这些消息传递给名叫file的处理器。
  - propaganda：true：的意思是，本记录器处理过的消息其他处理器也可以继续处理
- 现在消息来到名叫`file`的`handlers`中了。这个处理器定义了消息处理级别仍然为DEBUG，在class中定义将消息输出到文件中去，文件地址为项目目录的`logs/debug.log`。
- 因为这里没有配置`filters`和`formatters`，因此会采用默认的设置。

需要注意的是日志的输出文件的目录`logs/`一定要提前创建好，并且确保项目拥有此目录的写入权限。

这个日志系统就配置好了！接下来运行项目，随便刷新几个页面看看`debug.log`中有没有写入消息：

ERROR日志输出了整个bug的回溯，和你在浏览器中的报错是完全一样的，这些信息就非常的有用了。基本上error信息能够暴露出用户在使用你的网站过程中的大部分问题；也就是说每一个error都是需要你去解决掉的。error信息的错误吗d

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {# 格式化器verbose和simple
        'verbose': {# 详细的格式化器
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',# 依次输出：消息级别、发生时间、抛出模块、进程id、线程id、提示信息
            'style': '{',
        },
        'simple': {# 简要的格式化器
            'format': '{levelname} {message}',# 仅输出雄安锡级别和提示信息
            'style': '{',
        },
    },
    'filters': {# 过滤器
        'require_debug_true': {# 使用此过滤器的消息仅在调试的时候，才会生效
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {# 处理器
        'console': {
            'level': 'INFO',# 处理info以上级别的消息，输出简要信息到命令行；
            'filters': ['require_debug_true'],# 仅在调试模式生效
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',# 处理error以上级别的消息
            'class': 'django.utils.log.AdminEmailHandler',# 输出详细信息到email中
            'formatter': 'verbose',
        },
        'file': {
            'level': 'WARNING',# 处理warning以上级别消息
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),# 输出详细信息到文件中
            'formatter': 'verbose',
        },
    },
    'loggers': {# 记录器
        'django': {
            'handlers': ['console'],# 将django产生的所有消息转交给console处理器
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],# 将网络请求相关信息转交给file、mail_admins这两个处理器
            'level': 'WARNING',
            'propagate': False,# 记录器处理过的消息，就不再让django记录器再次处理了
        },
    }
}
```

**日志分割**

现在我们已经可以愉快的记录日志了，接下来一个问题是如何去**分割日志**？假设你的网站能够有幸运行十年时间，如果不间断的往同一个文件中写日志信息，最终它会变成一个拖垮服务器的庞然大物。

最好是日志能够按自然天进行记录和分割。好在这个问题也不需要你去费脑筋，Python帮你搞定了。

只需要把处理器稍稍改一下：

```python
my_blog/settings.py

...
LOGGING = {
    ...
    'handlers': {
        ...
        'file': {
            ...
            # 注释掉 class
            # 'class': 'logging.FileHandler',

            #新增内容
            'class': 'logging.handlers.TimedRotatingFileHandler',# python内置的随时间分割日志文件的模块
            'when': 'midnight',# 分割时间在凌晨
            'backupCount': 30,# 日志问价保存日期位30天

        },
    },
    ...
}
```

- `TimedRotatingFileHandler`：Python内置的随时间分割日志文件的模块
- `when`：分割时间为凌晨
- `backupCount`：日志文件保存日期为30天

接下来把系统时间往后调一天，然后重新启动服务器：

```
python manage.py runserver --noreload
```

**注意这次启动有点不一样**，后面有个`--noreload`后缀。这是因为通常Django的调试服务器运行时会顺带启动重载器，所以每当重载器检测到代码有变化后，会自动重启服务器，相当的方便。但问题是分割文件与重载器同时操作日志文件会产生冲突，因此这里一定要用`--noreload`暂时将重载器禁止掉。

然后就可以愉快的刷几条消息到文件中啦。你会发现老日志已经更名为`debug.log.2019-07-17`了，而刚刷的新消息则保存在`debug.log`中。

> 除了上面介绍的`TimedRotatingFileHandler`，Python还提供了一个按照文件大小分割的`RotatingFileHandler`。有兴趣的看[Python官方文档](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler)

**自定义日志**

内置配置实际上已经能够满足90%以上的日志需求了，但总有时候你想在一些奇怪的地方进行记录，这就需要你自己在代码中插入自定义的日志记录代码了。

自定义日志用起来也是相当方便的：

```python
from my_blog.settings import LOGGING
import logging

logging.config.dictConfig(LOGGING)
logger = loggering.getLogger('django.request')

def whatever(request):
    # do something
    logger.warning('something went wrong!')
    # do something else
```

导入刚才写的日志框架并将`django.request`配置到`logger`对象中。然后你就可以在任何地方安插任何级别的消息了。消息内容可以用字符串的格式化方法（`str.format()`），玩出各种花样。

关于日志的入门介绍就到此为止了，想深入学习的读者请继续阅读本文的参考文章：

- [Django logging](https://docs.djangoproject.com/en/2.2/topics/logging/)
- [Python 3 logging](https://docs.python.org/3/library/logging.html)





## 39-过滤器和标签









## 40-给文章点个赞









## 41-部署

#### 配置服务器

要架设网站，首先你要有一台连接到互联网的服务器。国内比较出名的云服务器属**阿里云**、**腾讯云**、**百度云**，三家各有优劣，大家自行了解比较，并选择自己适合的购买。

**利益相关：**博主自己用的是阿里云，所以教程会以**阿里云ECS**作为例子讲解。新用户通过[推广链接](https://www.aliyun.com/product/ecs?source=5176.11533457&userCode=m3bbolgr&type=copy)注册有折扣和现金券（目前是20元）；学生有[优惠服务器](https://promotion.aliyun.com/ntms/act/campus2018.html?source=5176.11533457&userCode=m3bbolgr&type=copy)每月9.5元，性能还不错，很划算。如果你想用其他云服务器，操作流程也差不多，不必担心。

首先进入**阿里云ECS的购买页面**：

<img src="D:\works\pactice\code_django\django_project\my_blog\图\屏幕截图(249).png" alt="img" style="zoom: 200%;" />

图片字很小，看不清楚的同学将就一下放大看吧。

挑重点说一下：

- **实例**从入门级里选一款便宜的，以后流量高了再升级也不迟（土豪请无视这条）。
- **镜像**选择 Ubuntu 16.04 64位。其他 Linux 版本也是可以的。
- **系统盘**先选个 20G，够你用一阵了。数据盘暂时用不上，不用勾选。

点击下一步，来到**网络和安全组**页面：

![img](http://blog.dusaiphoto.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%28250%29.png)

这页默认就行了，公网带宽选最低的 1M ，初期够用了。

点击下一步，到**系统配置**页面：

![img](http://blog.dusaiphoto.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%28241%29.png)

为了后面远程连接服务器更简单，这里勾选**自定义密码**，也就是输入用户/密码的认证方式了。实际上秘钥对的认证方式更安全些，以后摸熟了再改回来吧。

点击下一步，到**分组设置**页面。这个页面全部默认设置就好了。点击下一步，**确认订单**无误后，就可以付款啦。

付款成功后，通过控制台就可以看到已购买的云服务器了：

![img](http://blog.dusaiphoto.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%28243%29.png)

这里有时候会有黄字提醒你服务器的网络端口没开，点击黄字链接去开通一下：

![img](http://blog.dusaiphoto.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%28244%29.png)

把 22（远程连接端口）、443（HTTPS端口）、80（HTTP端口）都打开，3389端口顺便也开了。

至此服务器的购买、配置就完成啦。稍等几分钟后等待初始化完成，就可以得到服务器的**公网 IP 地址**，博主的是 `118.31.35.48` ，后面会用到。

接下来就是正式的部署。

#### 正式部署

开发时，我们用的是django自带的开发服务器，的那个性能太差了，不能用到线上环境。所以线上部署的时候，我们不仅要安装django，还要安装nginx和gunicorn，工作流程如下：

- 客户端发送给http请求，nginx作为直接对外的服务器接口，对http请求进行分析
- 如果是静态资源请求，则由nginx自己处理（效率很高）
- 如果是动态资源请求，则把它转发给gunicorn
- gunicorn对请求进行预处理后，转发给django，最终完成资源的返回

如果用餐馆来做比喻的话，Nginx 就是迎宾小姐，客人如果点了酒水，迎宾小姐自己就帮忙拿了；而 Gunicorn 是传菜员，Django 是厨师，他两一起满足客人对现炒美食的需求。

#### 远程连接

部署的第一步就是想办法连接到云服务器上去，否则一切都免谈。鉴于项目是在 Windows 环境开发的，推荐用 **XShell** 来作为远程连接的工具，非常的好用。XShell 有[学校及家庭版本](https://www.netsarang.com/zh/free-for-home-school/)，填一下姓名和邮箱就可以免费使用了。千万别嫌麻烦去下载来路不明的“绿色版”、“纯净版”，万一有木马你哭都哭不出来了。



连接成功后，就能在xshell窗口中看到阿里云的欢迎字样了。

```bash
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-151-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Welcome to Alibaba Cloud Elastic Compute Service !

root@dusaiphoto:~$ 
```

`root@dusaiphoto:~$`是命令提示符，输入命令时不需要你输入这个。本文后面把 `root@dusaiphoto:`字符省略掉，方便大家阅读。

#### 代码部署

为了防止系统太旧引起各种麻烦，先升级一下库的版本

```bash
~$ sudo apt-get update
~$ sudo apt-get upgrade
```

完成之后，接着安装需要的几个包：

```bash
sudo apt-get install nginx
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install git
sudo pip3 install virtualenv
```

分别安装了nginx、python3、pip、git、virtualenv。其中python3和pip3的写法是因为阿里云自带了python2.7，把它们区分一下。

之前开发的时候，虚拟环境用的是python自带的，为了避免读者的版本不同造成的各类错误，稳妥期间用virtualenv库来创建虚拟环境

接下来就是要改一下 Django 的配置文件 `settings.py`：

```python
my_blog/settings.py

# 关闭调试模式
DEBUG = False

# 允许的服务器
ALLOWED_HOSTS = ['*']

# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
```

- 部署的时候，要关闭调试模式，避免安全性问题（此时django就不在处理静态资源了）
- ALLOWED_HOSTS指明了允许访问的服务器名称或ip
  - 星号，表示允许所有的请求。
  - 实际部署的时候，改成你的域名或ip，比如`ALLOWED_HOSTS = ['.dusaiphoto.com', '127.0.0.1']`。
- 项目中有很多静态文件，部署时需要找一个地方统一收集起来，也就是`STATIC_ROOT`指定的地址了。

因为项目代码需要通过github仓库进行下载（）因为修改完毕后需要把代码上传到github，怎么上传这里也不赘述了，博主之前写过一篇[《Win 10 连接 GitHub》](https://www.dusaiphoto.com/article/detail/13/)的文章，有需要的读者稍微读一下。

**注意：一般情况下，需要将开发时生成的迁移文件（各个 app 中的 migrations 目录）一并上传到服务器端，这样可以保证各环境中的数据库操作一致。也就是说，服务器上不再需要 makemigrations 了，只进行 migrate 就可以了。这下理解为什么数据迁移要设计成两条指令了吧。**

**另外，**虚拟环境一般是需要在服务器上重新生成的**，因此我们需要把开发中用到的库列一个清单，以便在服务器上统一安装。在**本地虚拟环境**中输入：**

```bash
pip freeze > requirements.txt
```

项目中就多了个 `requirements.txt` 文件，里面记录了项目需要的库的清单。

然后更新 Git 记录并上传到 GitHub。重新回到**服务器的命令行**，给项目代码创建目录并进入此目录：

```
~$ mkdir -p /home/sites/dusaiphoto.com
~$ cd /home/sites/dusaiphoto.com
```

目录位置是随便你的，但建议找个地方统一管理所有的网站项目。

然后从 GitHub 中拉取项目代码：

```
../dusaiphoto.com$ git clone https://github.com/stacklens/django_blog_tutorial.git
```

这里拉取的博客教程的代码。建议读者先拉取教程代码来测试，成功之后再重新部署自己的代码。完成之后可以输入 `ls` 指令，看看代码文件夹是否正常生成了。

接着在服务器生成虚拟环境：

```
../dusaiphoto.com$ virtualenv --python=python3.5 env
../dusaiphoto.com$ source env/bin/activate
(env) ../dusaiphoto.com$ 
```

代码部署基本就完成了，接下来配置 `Nginx` 。

#### nginx

前面我们安装了 `Nginx` ，先来试试安装是否正常。启动 nginx 服务：

```
(env) ~$ sudo service nginx start
```

![img](D:\works\pactice\code_django\django_project\my_blog\图\屏幕截图(247).png)

Nginx 欢迎界面出现了，神奇吧。但这个默认配置显然是不能用的，所以需要重新写 Nginx 的配置文件。进入 `/etc/nginx/sites-available` 目录，这里是定义 **Nginx 可用配置**的地方。输入指令 `sudo vi dusaiphoto.com` 创建配置文件并打开 **vi 编辑器**：

```
(env) ~$ cd /etc/nginx/sites-available
(env) /etc/nginx/sites-available$ 
(env) /etc/nginx/sites-available$ sudo vi dusaiphoto.com
```

关于 `vi` 编辑器如何使用也不赘述了，这里只说两个最基本的操作：

- 按 `i` 键切换到**编辑模式**，这时候才可以进行输入、删除、修改等操作
- 按 `Ctrl + c` 退回到**命令模式**，然后输入 `:wq + Enter` 保存文件修改并退回到服务器命令行

回到正题，用 `vi` 在 `dusaiphoto.com` 文件中写入：

```
server {
  charset utf-8;
  listen 80;
  server_name 118.31.35.48;  # 改成你的 IP

  location /static {
    alias /home/sites/dusaiphoto.com/django_blog_tutorial/collected_static;
  }

  location /media {
    alias /home/sites/dusaiphoto.com/django_blog_tutorial/media;
  }

  location / {
    proxy_set_header Host $host;
    proxy_pass http://unix:/tmp/118.31.35.48.socket;  # 改成你的 IP
  }
}
```

此配置会监听80端口（通常http请求的端口），监听的ip地址写你自己的服务器公网ip

**配置中有三个规则：**

- 如果请求 static 路径则由 Nginx 转发到目录中寻找静态资源
- 如果请求 media 路径则由 Nginx 转发到目录中寻找媒体资源
- 其他请求则交给 Django 处理

> 如果你已经申请好域名了，就把配置中有 IP 的地方都修改为域名，比如：server_name www.dusaiphoto.com;

写好后就退出 `vi` 编辑器，回到命令行。因为我们写的只是 Nginx 的**可用配置**，所以还需要把这个配置文件链接到**在用配置**上去：

```
(env) ../sites-available$ sudo ln -s /etc/nginx/sites-available/dusaiphoto.com /etc/nginx/sites-enabled
```

至此 Nginx 就配置好了，接下来搞定 `Gunicorn`。

> 有的读者无论怎么配置都只能看到 Nginx 欢迎页面，有可能是 sites-enabled 目录中的 default 文件覆盖了你写的配置。将 default 文件删掉就可以正常代理自己的配置文件了。

#### gunicorn及测试

**先回到项目所在的目录**，并且进入**虚拟环境**，然后输入：

```
(env) ../django_blog_tutorial$ pip3 install gunicorn
(env) ../django_blog_tutorial$ sudo service nginx reload
(env) ../django_blog_tutorial$ gunicorn --bind unix:/tmp/118.31.35.48.socket my_blog.wsgi:application
```

这里的三个步骤分别是：

- 安装 `Gunicorn`
- 重启 `Nginx` 服务
- 启动 `Gunicorn`

> 启动 Gunicorn 也是一样，如果你已经有域名了，就把套接字中的 IP 地址换成域名；wsgi 字眼前面是项目的名称。另外 `sudo service nginx reload` 可替换成 `sudo service nginx restart`，区别是 reload 只重载配置文件，restart 重启整个服务。

接下来用浏览器访问服务器试一下：

![img](D:\works\pactice\code_django\django_project\my_blog\图\屏幕截图(251).jpg)









## 42-期末总结







## 43-小功能集合







## 44-读者常见问题