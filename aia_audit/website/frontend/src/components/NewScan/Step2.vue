<template>
    <div class="grid grid-cols-2 gap-4">
        <!-- Target Settings-->
        <div>
            <label class="block text-md font-medium text-blue-500 mb-4">
                Target
            </label>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-800">
                    Target Type
                </label>
                <div class="flex items-center">
                    <input v-model="targetType" id="target-type-1" name="target-type" type="radio" value=1 class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                    <label for="target-type-1" class="ml-2 text-sm font-medium text-gray-700 dark:text-gray-500">Host - Example: 192.168.56.2</label>
                </div>
                <div class="flex items-center">
                    <input v-model="targetType" id="target-type-2" name="target-type" type="radio" value=2 class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                    <label for="target-type-2" class="ml-2 text-sm font-medium text-gray-700 dark:text-gray-500">Network - Example: 192.168.56.0/24</label>
                </div>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-800">
                    Enter your target value:
                </label>
                <input v-model="target" type="text" id="target" class="w-3/4 bg-gray-50 border border-gray-300 text-gray-700 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" :placeholder="targetPlaceholder" required>
            </div>
        </div>
        <!-- Modules Settings -->
        <div>
            <label class="block text-md font-medium text-blue-500 mb-4">
                Modules
            </label>
            <div class="mb-4">
                <!-- Modules PickList-->
                <PickList v-model="products" dataKey="id" :showSourceControls="false" :showTargetControls="false">
                    <template #sourceheader>
                        Available
                    </template>
                    <template #targetheader>
                        Selected
                    </template>
                    <template #item="slotProps">
                        {{ slotProps.item.name }}
                    </template>
                </PickList>
            </div>
        </div>
    </div>
</template>

<script>
import PickList from 'primevue/picklist';

export default {
    components: {
        PickList
    },
    data() {
        return {
            products:[
                [
                    {id: 1, name: 'NMAP Module', module_type: 'Network Discovery'},
                    {id: 2, name: 'SSH Module', module_type: 'Vulnerability Scan'}
                ],
                [
                ]
            ]
        }
    },
    props: {
        target: String,
        targetType: Number,
        modules: Array
    },
    computed: {
        targetPlaceholder() {
            if(this.targetType == 1) return '192.168.203.100';
            else return '192.168.203.0/24';
        }
    },
}
</script>

<style>
.p-picklist .p-button{
    border: 1px solid #3b82f6!important; 
    background-color: #3b82f6!important;
}

.p-picklist .p-picklist-list .p-picklist-item.p-highlight{
    color: #3b82f6!important;
}

.p-picklist-header{
    font-size: 12px!important;
}
</style>