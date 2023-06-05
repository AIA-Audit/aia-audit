<template>
    <div class="bg-gray-800 text-white rounded-md px-4 py-4 h-96 overflow-y-scroll">
        <div v-for="line in content">
            <template v-if="line.type == 'status'">
                [<span class="text-yellow-500 font-bold">STATUS</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'info'">
                [<span class="text-blue-500 font-bold">INFO</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'success'">
                [<span class="text-green-500 font-bold">SUCCESS</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'warning'">
                [<span class="text-yellow-500 font-bold">WARNING</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'module'">
                [<span class="text-red-300 font-bold">MODULE</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'error'">
                [<span class="text-red-500 font-bold">ERROR</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'text'">
                <div class="text-white">
                    {{ line.value }}
                </div>
            </template>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            content: [
                {
                    type: 'status',
                    value: 'Connecting to the server socket...'
                },
            ]
        }
    },
    mounted() {
        var socketzg = this.socketio.io('http://localhost:8989');
        socketzg.on("message", this.handleMessage);

    },
    methods: {
        handleMessage(message) {
            this.content.push(
                {
                    type: message.type,
                    value: message.content
                }
            );
        }
    }
}


</script>