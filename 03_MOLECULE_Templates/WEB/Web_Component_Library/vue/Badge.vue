<template>
  <span class="ar-badge" :class="`ar-badge--${tone}`">
    <slot />
  </span>
</template>

<script setup>
// Badge — small status/category label.
// <Badge tone="success">Live</Badge>
defineProps({
  tone: { type: String, default: "neutral" }, // neutral | brand | info | success | warning | danger
});
</script>

<style>
@import "../../tokens/components.css";
</style>
