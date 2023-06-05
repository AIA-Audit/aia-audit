<template>
  <Steps :currentStep="currentStep" />
  <Navigation :scanType="scanType" :currentStep="currentStep" @nextStep="nextStep" @prevStep="prevStep" @startScan="startScan" />
  <Step1 ref="Step1" v-show="currentStep == 1" @setScanType="setScanType" />
  <Step2 ref="Step2" v-show="currentStep == 2" :scanType="scanType" :target="target" :targetType="targetType" :modules="modules" />
  <Step3 ref="Step3" v-show="currentStep == 3" />
</template>

<script>
import Navigation from '../components/NewScan/Navigation.vue'
import Steps from '../components/NewScan/Steps.vue'
import Step1 from '../components/NewScan/Step1.vue'
import Step2 from '../components/NewScan/Step2.vue'
import Step3 from '../components/NewScan/Step3.vue'
import { setTransitionHooks } from 'vue'
export default {
  components: {
    Navigation,
    Steps,
    Step1,
    Step2,
    Step3
  },
  data() {
    return {
      currentStep: 1,
      target: "",
      targetType: 1,
      modules: [[], []],
      scanType: 0
    }
  },
  mounted() {
    if(this.$parent.$parent._.data.status == 1) {
      this.currentStep = 3;
    }
    this.axios.get('/api/data/active-modules')
      .then(response => {
        this.modules[0] = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    nextStep() {
      if (this.validateStepData(this.currentStep)) {
        this.setStepData(this.currentStep);
        this.currentStep++;
      }
    },
    prevStep(data) {
      this.currentStep--;
    },
    setStepData(step) {
      if (step == 2) {
        this.target = this.$refs['Step' + step].target;
        this.targetType = this.$refs['Step' + step].targetType;
        this.modules = this.$refs['Step' + step].modules;
      }
    },
    setScanType(type) { 
      this.scanType = type;
      this.nextStep();
    },
    validateStepData(step) {
      if (step == 2) {
        if (this.$refs['Step' + step].target == "") {
          this.$toast.add({ severity: 'error', summary: 'Error Message', detail: 'Please, enter a target to scan', life: 3000 });
          return false;
        }
        if (this.scanType == 2 && this.$refs['Step' + step].modules[1].length == 0) {
          this.$toast.add({ severity: 'error', summary: 'Error Message', detail: 'Please, select at least one module', life: 3000 });
          return false;
        }
        return true;
      }
      else return true;
    },
    startScan() {
      this.$parent.$parent._.data.status = 1;
      console.log(this.scanType);
      this.axios.post('/api/scan/start', {
        target: this.target,
        targetType: this.targetType,
        modules: this.modules[1],
        type: this.scanType
      })
        .then(response => {
          if(response.data.status == "success") {
            this.$toast.add({ severity: 'success', summary: 'Success Message', detail: 'Scan completed successfully', life: 3000 });
            this.$parent.$parent._.data.status = 0;
          }
          else {
            this.$toast.add({ severity: 'error', summary: 'Error Message', detail: response.data.message, life: 3000 });
            this.$parent.$parent._.data.status = 0;
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
}
</script>

