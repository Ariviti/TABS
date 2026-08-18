<template>
  <div
    class="ar-card"
    :class="{ 'ar-card--interactive': interactive }"
    :role="interactive ? 'button' : undefined"
    :tabindex="interactive ? 0 : undefined"
  >
    <p v-if="eyebrow" class="ar-card__eyebrow">{{ eyebrow }}</p>
    <h3 v-if="title" class="ar-card__title">{{ title }}</h3>
    <p v-if="$slots.default && typeof $slots.default()[0]?.children === 'string'" class="ar-card__body">
      <slot />
    </p>
    <slot v-else />
  </div>
</template>

<script setup>
// Card — content container with optional eyebrow/title, or fully custom slot content.
// <Card eyebrow="Case Study" title="40% faster claims triage">Body copy.</Card>
defineProps({
  eyebrow: { type: String, default: "" },
  title: { type: String, default: "" },
  interactive: { type: Boolean, default: false },
});
</script>

<style>
@import "../../tokens/components.css";
</style>
