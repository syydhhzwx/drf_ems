import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login"
import Regist from "../components/Regist"
import Index from "../components/Emplist"
import AddEmo from "../components/AddEmp"
import UpdateEmp from "../components/UpdateEmp"

Vue.use(Router)

export default new Router({
  routes: [
    {path: '/login', component: Login},
    {path: '/register', component: Regist},
    {path: '/index', component: Index},
    {path: '/add', component: AddEmo},
    {path: '/update:id', component: UpdateEmp},
    {path: '/', redirect: "/login"},
    {path: '/*', redirect: "/login"},
  ]
})
