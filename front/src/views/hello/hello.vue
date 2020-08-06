<template>
  <div class="home">
   this is my hello HelloWorld
   <br>
    {{msg}}
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'hello',
  created(){
      console.log('created');
      

      // 这样就可以获取到全局变量
      let m = this.$store.state.msg;
      console.log(m);
  },
 data() {
    return {
      msg: "message"
    };
  }
 
}
</script>
