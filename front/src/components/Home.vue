<template>
    <v-app>
        <Banner></Banner>
        <v-content>
            <v-container>
                <goldlist :search="search" :key="search" v-on:update="search_Golds()" ></goldlist>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>

    import goldlist from './goldlist.vue';
    import Banner from './Banner.vue';
    import vue from 'vue';
    import {Authentique} from '../main.js';
    export default {
        name: 'home',
        components: {
            goldlist,Banner
        },
        data() {
            return {
            search: null,
            }
        },
        methods: {
            setAuthenticated(status) {
                this.authenticated = status;
            },
            logout() {
                this.authenticated = false;
            },
            search_Golds(){
            this.search=Authentique.search;
            console.log("Home",this.search)
            }
        },
        watch() {
            this.search=Authentique.search;
            console.log("Home",this.search);
            this.$router.go(this.$router.currentRoute)
        },
    };
</script>