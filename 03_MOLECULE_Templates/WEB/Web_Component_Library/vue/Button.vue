<template>
  <component
    :is="as"
    class="ar-btn"
    :class="[`ar-btn--${variant}`, size !== 'md' ? `ar-btn--${size}` : '']"
    :disabled="as === 'button' ? disabled : undefined"
    :aria-disabled="as !== 'button' ? disabled : undefined"
  >
    <slot />
  </component>
</template>

<script setup>
// Button — primary / secondary / ghost variants, 3 sizes.
// <Button variant="primary" @click="...">Get started</Button>
// <Button variant="ghost" size="sm" disabled>Not now</Button>
defineProps({
  variant: { type: String, default: "primary" }, // primary | secondary | ghost
  size: { type: String, default: "md" },          // sm | md | lg
  disabled: { type: Boolean, default: false },
  as: { type: String, default: "button" },
});
</script>

<style>
@import "../../tokens/components.css";
</style>
