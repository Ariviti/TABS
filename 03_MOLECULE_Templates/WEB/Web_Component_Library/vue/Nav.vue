<template>
  <nav class="ar-nav" aria-label="Primary">
    <a class="ar-nav__brand" :href="brandHref">
      <span class="ar-nav__brand-accent">a</span>riviti
    </a>
    <ul class="ar-nav__links">
      <li v-for="link in links" :key="link.href">
        <a
          class="ar-nav__link"
          :href="link.href"
          :aria-current="link.current ? 'page' : undefined"
        >{{ link.label }}</a>
      </li>
    </ul>
    <div v-if="$slots.actions" class="ar-nav__actions">
      <slot name="actions" />
    </div>
  </nav>
</template>

<script setup>
// Nav — top navigation bar with brand mark, links, and an action slot.
// <Nav :links="[{ label: 'Product', href: '/product' }]">
//   <template #actions><Button size="sm">Book a demo</Button></template>
// </Nav>
defineProps({
  links: { type: Array, default: () => [] }, // [{ label, href, current }]
  brandHref: { type: String, default: "/" },
});
</script>

<style>
@import "../../tokens/components.css";
</style>
