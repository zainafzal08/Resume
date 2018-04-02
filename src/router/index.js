import Vue from 'vue'
import Router from 'vue-router'
import Landing from '@/components/Landing'
import Notes from '@/components/Notes'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: Landing
    },
    {
      path: '/notes/:course',
      name: 'Notes',
      component: Notes
    },{
          path: '/notes/:course/:file',
          name: 'Notes',
          component: Notes
    },
    {
        path: '/notes',
        name: 'Notes',
        component: Notes
    }
  ]
})
