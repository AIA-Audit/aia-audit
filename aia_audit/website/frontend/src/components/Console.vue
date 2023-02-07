<template>
    <div class="bg-gray-800 text-white rounded-sm px-2 py-4 h-60">
        <div v-for="line in content">
            <template v-if="line.type == 'info'">
                [<span class="text-blue-500 font-bold">INFO</span>] {{ line.value }}
            </template>
            <template v-if="line.type == 'warning'">
                [<span class="text-yellow-500 font-bold">WARNING</span>] {{ line.value }}
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
                    type: 'info',
                    value: 'Waiting for scan to start..'
                },
            ]
        }
    }
}
</script>