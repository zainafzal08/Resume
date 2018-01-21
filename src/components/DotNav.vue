<template>
  <div class="nav-dots" :class="{focus:focused}">
    <div class="dots">
      <div v-for="i in dotNum" class="dot">
        <a class="mdi mdi-checkbox-blank-circle-outline" v-if="selected != i" v-on:click="registerClick(i)"></a>
        <a class="mdi mdi-checkbox-blank-circle" v-if="selected == i"></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DotNav',
  props: ['dotNum','trigger','selected','focused'],
  data () {
    return {}
  },
  methods: {
    registerClick: function(i) {
      this.trigger(i)
    }
  }
}
</script>

<style>
  .nav-dots {
    display: flex;
    width: 10vw;
    height: 100vh;
    position: absolute;
    align-items: center;
    z-index: 5;
  }

  .nav-dots .dots{
    width: 100%;
    text-align: center;
    font-size: 1.8rem;
    margin-left: 2rem;
    color: white;
    display: flex;
    flex-direction: column;
  }

  .nav-dots.focus {
    box-shadow: none;
  }

  .nav-dots .mdi-checkbox-blank-circle-outline:hover {
    opacity: 0.5;
  }

  .nav-dots .dots .dot {
    margin-bottom: 1rem;
  }
  @media screen and (max-width: 600px){
    .nav-dots {
      display: none;
    }
  }
</style>
