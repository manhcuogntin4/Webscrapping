<template>
    <v-app>
        <Banner></Banner>
        <v-content>
            <v-container>
                <goldlist :search="search" :key="search"></goldlist>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>

    import goldlist from './components/goldlist.vue';
    import Banner from './components/Banner.vue';


    export default {
        name: 'App',
        components: {
            goldlist,Banner
        },
        data() {
            return {
                searchAvailable: false,
                search: null,
                authenticated: false,
                mockAccount: {
                    username: "password",
                    password: "password"
                }
            }
        },
        watch() {
            this.search=Authentique.search;
            console.log(this.search);
        },
    };
</script>