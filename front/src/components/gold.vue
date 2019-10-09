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
                        <v-btn text icon color="red" @click="deleteGold">
                            <v-icon>mdi-delete</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['gold'],
        data: () => ({
            gold: null
        }),
        created() {
            axios.get('http://localhost:8000/api/v1/gold/' + this.gold.name).then((response) => {
                this.gold = response.data;
            });
        },
        methods: {
            deleteGold() {
                axios.delete('http://localhost:8000/api/v1/gold/' + this.gold.name);
            }
        }
    };
</script>