<template>
  <div class="poster-container">
    <!-- With < max elements they need to hover near middle -->

    <div id="nav-dots" class="nav-dots">
      <div class="dots">
        <div v-for="c in numCards">
          <a class="mdi mdi-checkbox-blank-circle-outline" v-if="card != c" v-on:click="updateCard(c)"></a>
          <a class="mdi mdi-checkbox-blank-circle" v-if="card == c"></a>
        </div>
      </div>
    </div>

    <div id ="card-1" class="poster-card poster-1 shadow">
      <div class="innards" id="card-1-innards">
        <div class="card-header">

        </div>
        <div class="card-content">

        </div>
        <div class="card-footer">

        </div>
      </div>
    </div>
    <div id ="card-2" class="poster-card poster-2 shadow">
      <div class="innards" id="card-2-innards">

      </div>
    </div>
    <div id ="card-3" class="poster-card poster-3 shadow">
      <div class="innards" id="card-3-innards">

      </div>
    </div>
  </div>
</template>

<script>
import './js/velocity.js'

export default {
  name: 'Landing',
  data () {
    return {
      animating: false,
      card: 1,
      numCards: 3,
      scrollThreshold: 15
    }
  },
  methods: {
    handleScroll (e) {
      if (e.deltaY > this.scrollThreshold && this.card < this.numCards) {
        this.nextCard(800,false)
      }
      if (e.deltaY < -1 * this.scrollThreshold  && this.card > 1) {
        this.prevCard(800,false)
      }
    },
    updateCard(c) {
      let adjust = (this.card > c) ? 1 : -1
      let target = this.card
      while(c != target) {
        if (adjust == 1) {
          this.prevCard(500,true)
        } else {
          this.nextCard(500,true)
        }
        c += adjust
      }
    },
    nextCard (d,ignoreState) {
      if (this.animating && !ignoreState) {
        return
      } else if (!ignoreState) {
        this.animating = true
        setTimeout(function() { this.animating = false }.bind(this), d+100)
      }
      window.Velocity(document.getElementById('card-' + this.card), {height: '0vh'}, d)
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '0'}, d)
      this.card++
    },
    prevCard (d,ignoreState) {
      if (this.animating) {
        return
      } else if (!ignoreState) {
        this.animating = true
        setTimeout(function() { this.animating = false }.bind(this), d+100)
      }
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '1'}, d)
      this.card--
      window.Velocity(document.getElementById('card-' + this.card), {height: '100vh'}, d)
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '1'}, d)
    }
  },
  created () {
    window.addEventListener('wheel', this.handleScroll)
  },
  destroyed () {
    window.removeEventListener('wheel', this.handleScroll)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Roboto|Source+Sans+Pro|Ubuntu');

  /* magic to capture all scroll events */
  .poster-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }

  .poster-card {
    width: 100vw;
    height: 100vh;
  }

  /* actual card components */
  .poster-card .card-header{
    width: 100%;
    height: 10%;
    display: flex;
  }
  .poster-card .card-content{
    width: 100%;
    height: 70%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Ubuntu', sans-serif;
    color: white;
  }
  .poster-card .card-content h1{
    font-size: 3rem;
  }
  .poster-card .card-footer{
    width: 100%;
    height: 20%;
    display: flex;
  }

  .poster-card .innards{
    width: 100%;
    height: 100%;
  }

  /* nav bar */
  .poster-container .nav-dots {
    display: flex;
    width: 10vw;
    height: 100vh;
    position: absolute;
    left: 2rem;
    align-items: center;
  }

  .poster-container .nav-dots a{
    margin-bottom: 1rem;
  }

  .poster-container .nav-dots .dots{
    width: 100%;
    text-align: center;
    font-size: 1.8rem;
    color: white;
    display: flex;
    flex-direction: column;
  }

  .poster-container .nav-dots .mdi-checkbox-blank-circle-outline:hover {
    opacity: 0.5;
  }
  /* poster background info */
  .poster-1 {
    background: #272B30;
  }
  .poster-2 {
    background-image: url('./images/poster_1.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
  }
  .poster-3 {
    background: #444444;
  }

  /* material design shadows */
  .shadow {
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  }

  .shadow:hover {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }
</style>
