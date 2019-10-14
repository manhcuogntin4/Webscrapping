<template>
    <v-container>
        <v-layout v-if="gold !== null">
            <v-flex xs12>
                <v-card class="mx-auto">
                    <v-list-item three-line>
                        <v-list-item-content>
                            <div class="overline mb-4">OVERLINE</div>
                            <v-list-item-title class="headline mb-1">{{ gold.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ gold.url }}</v-list-item-subtitle>
                            <v-list-item-subtitle>{{ gold.prix }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                         <v-btn text icon color="blue" @click="startEditGold">
                         <v-icon>mdi-pencil</v-icon>
                         </v-btn>
                        <v-btn text icon color="red" @click="deleteGold">
                            <v-icon>mdi-delete</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            <v-row justify="center">
                <v-dialog v-model="edit" persistent max-width="600px">
                    <v-card v-if="gold_edited">
                        <v-card-title class="mb-1">
                            <span class="display-1">{{ gold.name}}</span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                         <v-text-field :label="url" v-model="gold_edited.url"
                                                outlined
                                        >URL</v-text-field>
                                        <v-text-field :label="prix" v-model="gold_edited.prix"
                                                outlined
                                        >Prix</v-text-field>
                                </v-row>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <div class="flex-grow-1"></div>
                            <v-btn color="grey darken-1" text @click="edit = false">Close</v-btn>
                            <v-btn color="primary" @click="editGold">Save</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-row>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['gold'],
        data: () => ({
            edit: false,
            gold_edited: null,
        }),
        created() {
            axios.get('http://localhost:8000/api/v1/gold/' + this.gold.name).then((response) => {
                this.gold = response.data;
            });
        },
        methods: {
            deleteGold() {
                axios.delete('http://localhost:8000/api/v1/gold/' + this.gold.name);
            },
            startEditGold(){
            this.gold_edited={
                name:"",
                url:"",
                prix:0,
            };
             this.edit=true;
             this.prix=0;
             axios.get('http://localhost:8000/api/v1/gold/' + this.gold.name).then((response) => {
                    this.gold=response.data,
                    this.gold_edited.url=this.gold.url,
                    this.gold_edited.name=this.gold.name,
                    this.gold_edited.prix=this.gold.prix
                });
            },
            editGold() {
                axios.patch('http://localhost:8000/api/v1/gold/' + this.gold.name, this.gold_edited).then(() => {
                    this.$emit('update');
                    this.edit=false;
                });
            },
        }
    };
</script>