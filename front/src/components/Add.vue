<template>
    <v-app>
        <Banner></Banner>
        <v-content>
            <v-container>
             <v-form v-model="valid">
    <v-container>
       <v-card class="mx-auto" max-width="344">
        <v-card-title>
              Add new gold
        </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                             <v-text-field
                                            :label="name"
                                            v-model="gold_edited.name"
                                            outlined></v-text-field>
                            </v-row>
                            <v-row>
                                <v-col cols="12" sm="12" md="12" v-for="stat in Object.keys(gold_edited.stats)" :key="stat">
                                    <v-text-field
                                            :label="stat"
                                            v-model="gold_edited.stats[stat]"
                                            outlined
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <div class="flex-grow-1"></div>
                        <v-btn color="grey darken-1" text @click="go_Home()">Close</v-btn>
                        <v-btn color="primary" @click="save_gold()">Save</v-btn>
                    </v-card-actions>
     </v-card>
    </v-container>
  </v-form>

            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import axios from 'axios';

    import Banner from './Banner.vue';

    export default {
        name: 'add',
        components: {
            Banner
        },
        data:()=> ({
            gold_edited:{
            name:"",
            stats:
            {
                url:"",
                prix:0
            }

            }
        }),
        methods: {
        save_gold(){

          axios.post('http://localhost:8000/api/v1/gold/' + this.gold_edited.name, this.gold_edited.stats).then(() => {
                    console.log(this.gold_edited)
                });
        },
        go_Home() {
                this.$router.replace('/home');

            }
        }
    };
</script>