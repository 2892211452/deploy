<template>
<div class="home">
<p>{{title}}</p>
    <video
      id="video"
      class="video-js vjs-default-skin"
      controls
      preload="none"
      width="1200"
      :poster="imgUrl"
      data-setup="{}"
      v-bind:src="nowVideo"
    >
      <source type="video/mp4" />
    </video>

<div  block v-for="item in list" :key="item.message">
    <a-button type="primary" block     style="margin-top:10px" v-on:click="select(item.url)"
>
    {{item}}
      Primary
    </a-button 
    >

</div>
</div>



</template>

<script>
// @ is an alias to /src


export default {
  name: 'video',
  created(){
      console.log('created');
      

      // 这样就可以获取到全局变量
      let m = this.$store.state.msg;
      this.list =  this.$store.state.list;
      this.title =  this.$store.state.nowDm;
      this.imgUrl =  this.$store.state.imgUrl;
      console.log(m);
      this.nowVideo = this.list[0]['url']

      console.log(this.nowVideo);
       // this.Url="https://saas.jialingmm.net/code.php?type=flv&amp;vid=https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_3952b7fb97f0cf8a2f475ee16ea29c13.mp4&amp;userlink=http%3A%2F%2Fwww.imomoe.in%2Fplayer%2F7845-0-0.html&amp;adress=HuNan_ChangSha"
  },
 data() {
    return {
      msg: "message",
      imgUrl:'',
      nowVideo:"",
      list:[
        
      ]
    };
    
  },

 
  methods:{
      hello(){
        console.log('hello')
      },
      select(url){
          this.nowVideo=url;
          console.log(this.nowVideo)
        //   this.list.push('')
        //   this.list.pop()
      }
    }
 
}
</script>
