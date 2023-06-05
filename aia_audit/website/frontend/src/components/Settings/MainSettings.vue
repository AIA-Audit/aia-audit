<template>
    <h2 class="text-blue-700 text-xl font-bold">Main settings</h2>
    <div class="bg-gray-50 px-2 py-4 rounded-md">
        <div class="max-w-xl">
            <!-- Website IP Address -->
            <div class="my-4">
                <label for="website_address" class="block text-sm font-medium leading-6 text-gray-900">Website IP Address</label>
                <div class="mt-2">
                    <input type="text" v-model="website_address" id="website_address" class="w-3/4 border border-gray-300 text-gray-700 text-sm rounded-lg focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="0.0.0.0">
                </div>
            </div>
            <!-- Website Port -->
            <div class="my-4">
                <label for="website_port" class="block text-sm font-medium leading-6 text-gray-900">Website Port</label>
                <div class="mt-2">
                    <input type="text" v-model="website_port" id="website_port" class="w-3/4 border border-gray-300 text-gray-700 text-sm rounded-lg focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="5000">
                </div>
            </div>
            <!-- Telegram notify -->
            <div class="my-4">
                <label for="telegram_notify" class="block text-sm font-medium leading-6 text-gray-900">Notify via telegram</label>
                <div class="mt-2">
                    <InputSwitch v-model="telegram_notify"></InputSwitch>
                </div>
            </div>
            <!-- Telegram URL -->
            <div class="my-4">
                <label for="telegram_token" class="block text-sm font-medium leading-6 text-gray-900">Telegram URL</label>
                <div class="mt-2">
                    <input type="text" v-model="telegram_token" id="telegram_token" class="w-3/4 border border-gray-300 text-gray-700 text-sm rounded-lg focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
                </div>
            </div>
        </div>
    </div>
    <div class="flex justify-end">
        <button @click="saveSettings" class="mt-2 bg-green-500 text-white hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
            Save settings
        </button>
    </div>
</template>

<script>
import InputSwitch from 'primevue/inputswitch';
export default {
    components: {
        InputSwitch
    },
    data() {
        return  {
            website_address: '',
            website_port: '',
            telegram_notify: false,
            telegram_token: '',
        }
    },
    mounted(){
        this.axios.get('/api/data/config').then((response) => {
            this.website_address = response.data.website_address;
            this.website_port = response.data.website_port;
            this.telegram_notify = response.data.telegram_notify.toLowerCase() == 'true' ? true : false;
            this.telegram_token = response.data.telegram_token;
        });
    },
    methods: {
        saveSettings() {
            if(!this.validateForm()) return;
            this.axios.post('/api/data/config', {
                website_address: this.website_address,
                website_port: this.website_port,
                telegram_notify: this.telegram_notify,
                telegram_token: this.telegram_token,
            }).then((response) => {
                if(response.data.status == 'success') {
                    this.$toast.add({
                        severity: 'success',
                        summary: 'Success',
                        detail: 'Settings saved successfully',
                        life: 3000
                    });
                } else {
                    this.$toast.add({
                        severity: 'error',
                        summary: 'Error',
                        detail: 'Failed to save settings',
                        life: 3000
                    });
                }
            });
        },
        validateForm(){
            if(this.telegram_notify && this.telegram_token == '') {
                this.$toast.add({
                    severity: 'error',
                    summary: 'Error',
                    detail: 'Telegram URL is required',
                    life: 3000
                });
                return false;
            }
            return true;
        }
    }
}
</script>