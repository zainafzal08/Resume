<template>
  <div class="footer">
    <div class="content">
      <h1> Connect With Me! </h1>
      <br>
      <div class="socials">
        <div class="link" v-for="link in socialLinks">
          <a :href="link.link" :class="'mdi mdi-'+link.icon"></a>
        </div>
      </div>
    </div>
    <div class="love">
      <span>Made With <a style="color: red" class="mdi mdi-heart" href=""></a> In <a style="color: #4fc08d" href="https://vuejs.org/" class="mdi mdi-vuejs"></a></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  props: ["title","socialLinks"],
  data () {
    return {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Roboto|Source+Sans+Pro|Ubuntu');

  .footer {
    width: 40vw;
    height: 100vh;
    text-align: center;
    font-family: 'Ubuntu',sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }

  .footer .content {
    width: 100%;
  }

  .footer .love {
    position: absolute;
    bottom: 2rem;
  }

  .footer h1{
    font-size: 3rem;
    margin-top: 0;
  }

  .footer .socials {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    font-size: 2rem;
  }
  .footer .socials a{
    color: white;
    opacity: 0.4;
  }
  .footer .socials a:hover{
    color: white;
    opacity: 1;
  }
  .footer .socials .link{
    display: flex;
    align-items: center;
    justify-content: center;
  }
  @media screen and (max-width: 600px){
    .footer {
      width: 90vw;
      text-align: center;
      font-family: 'Ubuntu',sans-serif;
    }
  }
</style>
