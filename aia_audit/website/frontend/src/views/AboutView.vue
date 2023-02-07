<template>
    <div class="mx-auto max-w-7xl py-12 px-6 lg:px-8 lg:py-24">
      <div class="space-y-12">
        <div class="space-y-5 sm:space-y-4 md:max-w-xl lg:max-w-3xl xl:max-w-none">
          <h2 class="text-3xl font-bold tracking-tight text-gray-800 sm:text-4xl">About us</h2>
          <p class="text-xl text-gray-700">
            This project is designed to make cybersecurity auditories more efficient, reliable and accessible. We have designed a tool that is easy to use and which will significantly reduce the time it takes to complete an audit. It automates many of the tedious processes associated with conducting a cybersecurity audit and simplifies the process for everyone involved.
          </p>
        </div>
        <ul role="list" class="space-y-4 sm:grid sm:grid-cols-2 sm:gap-6 sm:space-y-0 lg:grid-cols-3 lg:gap-8">
          <li v-for="person in people" :key="person.name" class="rounded-lg bg-gray-800 py-10 px-6 text-center xl:px-10 xl:text-left">
            <div class="space-y-6 xl:space-y-10">
              <img class="mx-auto h-40 w-40 rounded-full xl:h-56 xl:w-56" :src="person.imageUrl" alt="" />
              <div class="space-y-2 xl:flex xl:items-center xl:justify-between">
                <div class="space-y-1 text-lg font-medium leading-6">
                  <h3 class="text-white">{{ person.name }}</h3>
                  <p class="text-blue-500">{{ person.role }}</p>
                </div>

                <ul role="list" class="flex justify-center space-x-5">
                  <li>
                    <a :href="person.githubUrl" class="text-gray-400 hover:text-gray-300">
                      <span class="sr-only">Github</span>
                      <svg fill="white" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
</template>

<script setup>
const people = [
  {
    name: 'Ismael Semmar Galvez',
    role: 'Senior Designer',
    imageUrl:
      'https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80',
    githubUrl: '#',
  },
  {
    name: 'Andreu Gisbert Bel',
    role: 'Senior Designer',
    imageUrl:
      'https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80',
    githubUrl: '#',
  },
  {
    name: 'Andreu Monforte',
    role: 'Senior Designer',
    imageUrl:
      'https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=1024&h=1024&q=80',
    githubUrl: '#',
  },
]
</script>