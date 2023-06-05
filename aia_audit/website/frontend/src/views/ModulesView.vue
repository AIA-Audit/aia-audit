<template>
    <DataTable v-model:expandedRows="expandedRows" :value="modules" paginator :rows="5">
        <!-- If current item is installed show expand -->
        <Column expander style="width: 5rem" />
        <Column field="name" header="Name"></Column>
        <Column field="author" header="Author"></Column>
        <Column field="version" header="Version"></Column>
        <Column field="installed" header="Installed">
            <template #body="slotProps">
                <i class="pi pi-check text-green-500" v-if="slotProps.data.installed == 'yes'"></i>
                <i class="pi pi-times text-red-500" v-else></i>
            </template>
        </Column>
        <Column field="" header="Actions">
            <template #body="slotProps">
                <button @click="installModule(slotProps.data.dirname)"
                    class="lg:w-full text-center bg-green-500 text-white hover:bg-green-600 px-4 py-2"
                    v-if="slotProps.data.installed == 'no'">Install</button>
                <button @click="uninstallModule(slotProps.data.name)"
                    class="lg:w-full text-center text-white bg-red-500 hover:bg-red-600 px-4 py-2" v-else>Uninstall</button>
            </template>
        </Column>
        <template #empty> No modules found </template>
        <template #expansion="slotProps">
                <!-- Template if object has atleast 1 item -->
                <template v-if="Object.keys(slotProps.data.module_settings).length > 0">
                <h3 class="text-lg font-bold">Module Settings</h3>
                <template v-for="(field, index) in slotProps.data.module_settings">
                    <template v-if="field.type == 'textbox'">
                        <div class="relative my-2">
                            <label for="name" class="block text-sm font-medium leading-6 text-gray-900">{{ field.name }}</label>
                            <input type="text" v-model="field.value" id="name"
                                class="block w-full rounded-md border-0 text-blue-500 px-3 py-3 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 sm:text-sm sm:leading-6"
                                :placeholder="field.placeholder" :disabled = "slotProps.data.installed == 'no'" v-bind:class="{ 'bg-gray-100 cursor-not-allowed': slotProps.data.installed == 'no' }">
                        </div>
                    </template>
                    <template v-if="field.type == 'checkbox'">
                        <div class="space-y-5 my-2">
                            <div class="relative flex items-start">
                                <div class="flex h-6 items-center">
                                    <input id="comments" aria-describedby="comments-description" v-model="field.value" type="checkbox"
                                        class="h-4 w-4 rounded border-gray-300 text-blue-500" :disabled = "slotProps.data.installed == 'no'" v-bind:class="{ 'bg-gray-100 cursor-not-allowed': slotProps.data.installed == 'no' }">
                                </div>
                                <div class="ml-3 text-sm leading-6">
                                    <label for="comments" class="font-medium text-blue-500">
                                        {{ field.name }}
                                    </label>
                                </div>
                            </div>
                        </div>
                    </template>
                    <button @click="saveModuleSettings(slotProps.data.name, slotProps.data.module_settings)" v-if="slotProps.data.installed == 'yes'"
                        class="mt-2 bg-green-500 text-white hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                        Save settings
                    </button>
                </template>
            </template>
            <template v-else>
                <h3 class="text-md">No settings available for this module</h3>
            </template>
        </template>
    </DataTable>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional

export default {
    components: {
        DataTable,
        Column,
        ColumnGroup,
        Row
    },
    data() {
        return {
            modules: [],
            expandedRows: []
        }
    },
    mounted() {
        this.axios.get('/api/data/modules').then(response => {
            this.modules = response.data;
        })
    },
    methods: {
        installModule(moduleName) {
            this.axios.post('/api/install-module', {
                module: moduleName
            }).then(response => {
                if (response.data.status == 'success') {
                    this.$toast.add({
                        severity: 'success',
                        summary: 'Success',
                        detail: 'Module installed successfully',
                        life: 3000
                    });
                    for (let i = 0; i < this.modules.length; i++) {
                        if (this.modules[i].dirname == moduleName) {
                            this.modules[i].installed = 'yes';
                            break;
                        }
                    }
                } else {
                    this.$toast.add({
                        severity: 'error',
                        summary: 'Error',
                        detail: 'Failed to install module',
                        life: 3000
                    });
                }
            });
        },
        uninstallModule(moduleName) {
            this.axios.post('/api/uninstall-module', {
                module: moduleName
            }).then(response => {
                if (response.data.status == 'success') {
                    this.$toast.add({
                        severity: 'success',
                        summary: 'Success',
                        detail: 'Module uninstalled successfully',
                        life: 3000
                    });
                    for (let i = 0; i < this.modules.length; i++) {
                        if (this.modules[i].name == moduleName) {
                            this.modules[i].installed = 'no';
                            break;
                        }
                    }
                } else {
                    this.$toast.add({
                        severity: 'error',
                        summary: 'Error',
                        detail: 'Failed to uninstall module',
                        life: 3000
                    });
                }
            });
        },
        saveModuleSettings(moduleName, settings) {
            this.axios.post('/api/save-module-settings', {
                module: moduleName,
                settings: settings
            }).then(response => {
                if (response.data.status == 'success') {
                    this.$toast.add({
                        severity: 'success',
                        summary: 'Success',
                        detail: 'Module settings saved successfully',
                        life: 3000
                    });
                } else {
                    this.$toast.add({
                        severity: 'error',
                        summary: 'Error',
                        detail: 'Failed to save module settings',
                        life: 3000
                    });
                }
            });
        }
    }
}
</script>