<template>
  <div class="poster-container">
    <DotNav :bg="theme" :dotNum="cards.length" :trigger="updateCard" :selected="card" :focused="card == 1"></DotNav>

    <Card name="card-1" suffix="-innards" :bg="theme" bgt="color">
      <TitleBrand title="Zain Afzal" :colors="pallet"></TitleBrand>
    </Card>

    <Card name="card-2" suffix="-innards" :bg="require('./images/poster_1.jpeg')" bgt="image">
      <ProjectOutline title="Image Scrapers" :bg="theme" :theme="pallet[2]" :points="cardData.imageScraper"></ProjectOutline>
    </Card>

    <Card name="card-3" suffix="-innards" :bg="require('./images/poster_2.png')" bgt="image">
      <ProjectOutline title="Web Dev" :bg="theme" :theme="pallet[0]" :points="cardData.webDev"></ProjectOutline>
    </Card>

    <Card name="card-4" suffix="-innards" :bg="require('./images/poster_3.jpeg')" bgt="image">
      <ProjectOutline title="Low Level" :bg="theme" :theme="pallet[3]" :points="cardData.lowLevel"></ProjectOutline>
    </Card>

    <Card name="card-5" suffix="-innards" :bg="require('./images/poster_4.png')" bgt="image">
      <ProjectOutline title="Misc" :bg="theme" :theme="pallet[1]" :points="cardData.misc"></ProjectOutline>
    </Card>

    <Card name="card-6" suffix="-innards" :bg="theme" bgt="color">
      <Footer :socialLinks="socials" :colors="pallet"></Footer>
    </Card>

  </div>
</template>

<script>
import DotNav from './DotNav.vue'
import TitleBrand from './TitleBrand.vue'
import Card from './Card.vue'
import ProjectOutline from './ProjectOutline.vue'
import Footer from './Footer.vue'

export default {
  name: 'Landing',
  data () {
    return {
      animating: false,
      pallet: [
        "#d9534f",
        "#29ABE0",
        "#F47C3C",
        "#93C54B"
      ],
      cards: [
        ["card-1","card-1-innards"],
        ["card-2","card-2-innards"],
        ["card-3","card-3-innards"],
        ["card-4","card-4-innards"],
        ["card-5","card-5-innards"],
        ["card-6","card-6-innards"]
      ],
      socials: [
        {link: "https://github.com/zainafzal08", icon: "github-circle"},
        {link: "https://twitter.com/NubmerOneHo", icon: "twitter"},
        {link: "https://www.linkedin.com/in/zain-afzal-561262117/", icon: "linkedin"},
        {link: "mailto:zain.afz@gmail.com", icon: "email"}
      ],
      card: 1,
      lastY: -1,
      scrollThreshold: 15,
      theme: "#272B30",
      cardData: {
        imageScraper:[
          {
            title: "Pixel Scraper",
            description: "A small script to search and find royalty free images from pexels landscape images.",
            links: [{link: "https://github.com/zainafzal08/CoolStuff/blob/master/Scripts/Image%20Scrapers/Pexel.py", icon: "github-circle"}]
          },
          {
            title: "NatGeo Scraper",
            description: "A small script to search and find images from National Geographics Image Archives given constraints.",
            links: [{link: "https://github.com/zainafzal08/CoolStuff/blob/master/Scripts/Image%20Scrapers/NatGeo.py", icon: "github-circle"}]
          },
          {
            title: "Reddit Scraper",
            description: "A small script to search and find a beautiful image from reddit given constraints.",
            links: [{link: "https://github.com/zainafzal08/CoolStuff/blob/master/Scripts/Image%20Scrapers/NatGeo.py", icon: "github-circle"}]
          }
        ],
        webDev: [
          {
            title: "UNSW Sec Soc",
            description: "The UNSW Security Society Website built with jekyll and the bootswatch 'lux' theme",
            links: [{link: "http://www.unswsecurity.com/", icon: "web"}]
          },
          {
            title: "Subleq",
            description: "A puzzle game revolving around a single instruction set arcitecture machine built with a friend",
            links: [
              {link: "http://subleq.herokuapp.com/", icon: "web"}
            ]
          },
          {
            title: "This Site!",
            description: "The Vue components used in this very site!",
            links: [{link: "https://github.com/zainafzal08/Resume", icon: "github-circle"}]
          }
        ],
        lowLevel: [
          {
            title: "General Vm",
            description: "A custom designed instruction set, run in python",
            links: [{link: "https://github.com/zainafzal08/General_VM", icon: "github-circle"}]
          },
          {
            title: "BF Machine",
            description: "A debugging/runtime environment for the BF esoteric programming language",
            links: [{link: "https://github.com/zainafzal08/BF-Machine", icon: "github-circle"}]
          },
          {
            title: "Generic Data",
            description: "Some basic code in C to create a abstract data structure at run time",
            links: [{link: "https://github.com/zainafzal08/GenericData", icon: "github-circle"}]
          }
        ],
        misc: [
          {
            title: "Hex Generator",
            description: "js that outputs a svg hexagon pattern with a custom gradient",
            links: [{link: "https://codepen.io/zainafzal08/pen/EoqZVN", icon: "codepen"}]
          },
          {
            title: "Notes",
            description: "Markdown notes for some of the courses i've taken at UNSW",
            links: [{link: "https://github.com/zainafzal08/Notes", icon: "github-circle"}]
          },
          {
            title: "Hodge Podge",
            description: "A small discord bot to send memes, roll dice and search DnD spells!",
            links: [{link: "https://github.com/zainafzal08/HodgePodge", icon: "github-circle"}]
          }
        ]
      }
    }
  },
  components: {
    DotNav,
    TitleBrand,
    Card,
    ProjectOutline,
    Footer
  },
  mounted: function(){
    for(var card in this.cards){
      if (card != 0)
        document.getElementById(this.cards[card][1]).style.opacity = '0';
    }
  },
  methods: {
    handleScroll (e) {
      if (e.deltaY > this.scrollThreshold && this.card < this.cards.length ) {
        this.nextCard(800,false)
      }
      if (e.deltaY < -1 * this.scrollThreshold  && this.card > 1 ) {
        this.prevCard(800,false)
      }
    },
    handleTouchStart(e) {
      if (e.touches.length > 1)
        return
      this.lastY = e.touches[0].clientY;
    },
    handleTouchEnd(e) {
      if (e.touches.length > 1)
        return
      var currentY = e.changedTouches[0].clientY
      var val = this.lastY - currentY
      var diff = Math.abs(this.lastY - currentY)
      if ( diff > this.scrollThreshold && val < 0) {
        this.prevCard(800,false)
      } else if (diff > this.scrollThreshold && val > 0) {
        this.nextCard(800,false)
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
      window.Velocity(document.getElementById(this.cards[this.card-1][0]), {'margin-top': '-100vh'}, d)
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '0'}, d)
      this.card++
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '1'}, d)
    },
    prevCard (d,ignoreState) {
      if (this.animating && !ignoreState) {
        return
      } else if (!ignoreState) {
        this.animating = true
        setTimeout(function() { this.animating = false }.bind(this), d+100)
      }
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '0'}, d)
      this.card--
      window.Velocity(document.getElementById(this.cards[this.card-1][0]), {'margin-top': '0vh'}, d)
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '1'}, d)
    }
  },
  created () {
    window.addEventListener('wheel', this.handleScroll)
    document.addEventListener('touchstart',this.handleTouchStart, false)
    document.addEventListener('touchend',this.handleTouchEnd, false)
  },
  destroyed () {
    window.removeEventListener('wheel', this.handleScroll)
    document.removeEventListener('touchstart',this.handleTouchStart)
    document.removeEventListener('touchend',this.handleTouchEnd)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /* Container  */
  .poster-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }
</style>
