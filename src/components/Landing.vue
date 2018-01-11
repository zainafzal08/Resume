<template>
  <div class="poster-container">
    <div id ="card-1" class="poster-card poster-1 shadow">
      <div class="innards" id="card-1-innards">
        <div class="card-header">

        </div>
        <div class="card-content">
          <div class="center-text">
            <h1> Zain Afzal </h1>
            <hr>
            <div class="logos">

            </div>
            <h3> He's alright i guess </h3>
          </div>
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
      if (e.deltaY > this.scrollThreshold && !this.animating && this.card < this.numCards) {
        this.animating = true
        setTimeout(function() {
          this.animating = false
        }.bind(this), 1000)
        this.nextCard()
      }
      if (e.deltaY < -1 * this.scrollThreshold && !this.animating && this.card > 1) {
        this.animating = true
        setTimeout(function() {
          this.animating = false
        }.bind(this), 1000)
        this.prevCard()
      }
    },
    nextCard () {
      window.Velocity(document.getElementById('card-' + this.card), {height: '0vh'}, 800)
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '0'}, 800)
      this.card++
    },
    prevCard () {
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '1'}, 800)
      this.card--
      window.Velocity(document.getElementById('card-' + this.card), {height: '100vh'}, 800)
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '1'}, 800)
    },
    jumpCard (c) {

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
    font-family:  'Ubuntu', sans-serif;
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

  .poster-card .logos{
    text-align: center;
    width: 50%;
  }

  .poster-card .center-text{
    text-align: center;
    width: 50%;
  }
  .poster-card .innards{
    width: 100%;
    height: 100%;
  }
  /* poster background info */
  .poster-1 {
    background: #444444;
  }
  .poster-2 {
    background-image: url('./images/poster_1.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
  }
  .poster-3 {
    background: #EBEBEB;
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
