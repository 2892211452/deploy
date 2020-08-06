<template>
  <div class="home">
    <a-input-search
      placeholder="input search text"
      enter-button="Search"
      size="large"
      v-model ="keyword" 
      @search="search_click"
    />

    <div id='card'>
            <a-card hoverable style="width: 240px">
            <img
            slot="cover"
            alt="example"
            src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
            />
            <a-card-meta title="Europe Street beat">
            <template slot="description">
                www.instagram.com
            </template>
            </a-card-meta>
        </a-card>

  
    </div>


  </div>
  
</template>

<script>
// @ is an alias to /src


export default {
  name: 'main',
  created(){
      console.log('created');
      

      // 这样就可以获取到全局变量
      let m = this.$store.state.msg;
      console.log(m);
  },
 data() {
    return {
      msg: "message",
      keyword:''
      
    };

   
  },
  methods: {
      search_click(){
          console.log('ckick')
          console.log(this.keyword)
          if(this.keyword ==''){
              alert('error')
          }
          var data = null;
            //获取数据
            var xhr = new XMLHttpRequest();
            xhr.withCredentials = true;

            xhr.addEventListener("readystatechange", function () {
              if (this.readyState === 4) {
                console.log(this.responseText);
              }
            });

            xhr.open("GET", "http://127.0.0.1:5000/search?name=%E7%81%AB%E5%BD%B1");
            xhr.setRequestHeader("cache-control", "no-cache");
            xhr.setRequestHeader("postman-token", "b63630d6-1dbc-4bf0-bb31-8f3422b0e25e");

            xhr.send(data);




      }

  }
 
}
</script>
