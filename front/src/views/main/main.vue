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
      }

  }
 
}
</script>
