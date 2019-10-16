import Vue from 'vue'
import Router from 'vue-router'
import LoginComponent from "./components/Login.vue"
import HomeComponent from "./components/Home.vue"
import AboutComponent from "./components/About.vue"
import AddComponent from "./components/Add.vue"
import App from "./App.vue"

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: "/login",
            name: "login",
            component: LoginComponent
        },
        {
            path: "/home",
            name: "home",
            component: HomeComponent
        },
        {
            path: "/about",
            name: "about",
            component: AboutComponent
        },
        {
            path: "/add",
            name: "add",
            component: AddComponent
        },
        {
            path: '/',
            redirect: {
                name: "login"
            }
        },
    ]
})