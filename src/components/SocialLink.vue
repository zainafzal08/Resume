<template>
  <div class="socialLink" v-on="{mouseover: mouseOver,mouseleave: mouseLeave}">
      <a :href="link" :class="'mdi mdi-'+icon" :style="{'color': getColor()}"></a>
  </div>
</template>

<script>
export default {
  name: 'socialLink',
  props: ['link','icon','color','routerLink'],
  data () {
    return {
      hovered: false
    }
  },
  methods: {
    getColor: function() {
      if (this.hovered) {
        return this.color;
      } else {
        return "#666666";
      }
    },
    mouseOver: function(){
      this.hovered = true;
    },
    mouseLeave: function(){
      this.hovered = false;
    }
  }
}
</script>

<style>
.socialLink {
  font-size: 2rem;
}
.socialLink a:hover{
  opacity: 0.9;
}
</style>
