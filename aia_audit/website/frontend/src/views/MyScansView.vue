<template>
    <DataTable :value="scans" paginator :rows="5">
        <Column field="id" header="Code"></Column>
        <Column field="name" header="Name"></Column>
        <Column header="Started at">
        <template #body="slotProps">
            {{ unixToTimestamp(slotProps.data.start_time) }}
        </template>
        </Column>
        <Column header="End at">
        <template #body="slotProps">
            {{ unixToTimestamp(slotProps.data.end_time) }}
        </template>
        </Column>
        <Column field="target" header="target"></Column>
        <Column header="">
            <template #body="slotProps">
                <div class="flex justify-center">
                    <router-link :to="{ name: 'scan', params: { id: slotProps.data.id } }" class="text-center text-white bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-md">View results</router-link>
                </div>
            </template>
        </Column>
        <template #empty> No scans performed yet </template>
    </DataTable>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional

export default{
    components: {
        DataTable,
        Column,
        ColumnGroup,
        Row
    },
    data(){
        return {
            scans: []
        }
    },
    mounted(){
        this.axios.get('/api/data/scans').then((response) => {
            console.log(response.data);
            this.scans = response.data;
        });
    },
    methods: {
        unixToTimestamp(unixdate) {
            console.log(unixdate);
            return this.moment.unix(unixdate).format('DD/MM/YYYY HH:mm:ss');
        }
    }
}
</script>