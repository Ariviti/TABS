<template>
  <div class="ar-alert" :class="`ar-alert--${tone}`" role="status">
    <span class="ar-alert__icon" aria-hidden="true">{{ icon }}</span>
    <div>
      <p v-if="title" class="ar-alert__title">{{ title }}</p>
      <p class="ar-alert__body"><slot /></p>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

// Alert — inline status callout.
// <Alert tone="warning" title="Review required">This affects production data.</Alert>
const props = defineProps({
  tone: { type: String, default: "info" }, // info | success | warning | danger
  title: { type: String, default: "" },
});

const ICONS = { info: "i", success: "\u2713", warning: "!", danger: "\u2715" };
const icon = computed(() => ICONS[props.tone]);
</script>

<style>
@import "../../tokens/components.css";
</style>
