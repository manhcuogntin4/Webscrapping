<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <span>Gold Comparater</span>
            </v-toolbar-title>
        </v-app-bar>

        <v-content>
            <gold name="100"/>
            <gold name="200"/>
        </v-content>
    </v-app>
</template>

<script>

    import gold from './components/gold';

    export default {
        name: 'App',
        components: {
            gold,
        },
        data: () => ({//
        }),
    };
</script>