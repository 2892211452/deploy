# 搭建vue的demo项目


运行以下命令来创建一个新项目：
```
vue create hello-world
```


![](https://i.imgur.com/s9bVkPZ.png)


**可以直接选择，也可以手动npm安装**



# vuehello

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).




# 开发思路
- 使用vue router去进行路由控制，跳转的一些把控
- vuex可以用来进行全局变量管理
- 使用localstorage进行浏览器本地变量管理，可以实现跨页面通信。
- 使用axios进行请求