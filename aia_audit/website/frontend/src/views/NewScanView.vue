<template>
  <Steps :currentStep="currentStep" />
  <Navigation :scanType="scanType" :currentStep="currentStep" @nextStep="nextStep" @prevStep="prevStep" />
  <Step1 ref="Step1" v-show="currentStep == 1" @setScanType="setScanType"/>
  <Step2 ref="Step2" v-show="currentStep == 2" :target="target" :targetType="targetType" :modules="modules"/>
  <Step3 ref="Step3" v-show="currentStep == 3"/>
</template>

<script>
  import Navigation from '../components/NewScan/Navigation.vue'
  import Steps from '../components/NewScan/Steps.vue'
  import Step1 from '../components/NewScan/Step1.vue'
  import Step2 from '../components/NewScan/Step2.vue'
  import Step3 from '../components/NewScan/Step3.vue'
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
        modules:[[{id: 1, name: 'NMAP Module', module_type: 'Network Discovery'}],[]],
        scanType: 0
      }
    },
    methods: {
      nextStep() {
        if(this.validateStepData(this.currentStep)){
          this.setStepData(this.currentStep);
          this.currentStep++;
        }
      },
      prevStep(data) {
        this.currentStep--;
      },
      setStepData(step){
        if(step == 2){
          this.target = this.$refs['Step' + step].target;
          this.targetType = this.$refs['Step' + step].targetType;
          this.modules = this.$refs['Step' + step].modules;
        }
      },
      setScanType(type) {
        if(type == 1 || type == 2) return;
        this.scanType = type;
        this.nextStep();
      },
      validateStepData(step){
        /* Step 2 Validation */
        if(step == 2){
          if(this.$refs['Step' + step].target == ""){
            this.$toast.add({severity:'error', summary: 'Error Message', detail:'Please, enter a target to scan', life: 3000});
            return false;
          }
          if(this.$refs['Step' + step].modules[1].length == 0){
            this.$toast.add({severity:'error', summary: 'Error Message', detail:'Please, select at least one module', life: 3000});
            return false;
          }
          return true;
        }
        /* For now, only Step 2 is validated, if not Step 2 then return true */
        else return true;
      },

    }
  }
</script>

