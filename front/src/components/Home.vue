<template>
    <v-app>
        <Banner></Banner>
        <v-content>
            <v-container>
                <goldlist :search="search"></goldlist>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>

    import goldlist from './goldlist.vue';
    import Banner from './Banner.vue';


    export default {
        name: 'home',
        components: {
            goldlist,Banner
        },
        data() {
            return {
                searchAvailable: false,
                search: null,
                authenticated: false,
                mockAccount: {
                    username: "nraboy",
                    password: "password"
                }
            }
        },
        methods: {
            setAuthenticated(status) {
                this.authenticated = status;
            },
            logout() {
                this.authenticated = false;
            }
        }
    };
</script>