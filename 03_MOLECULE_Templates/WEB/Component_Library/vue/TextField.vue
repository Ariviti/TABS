<template>
  <div class="ar-field">
    <label v-if="label" class="ar-field__label" :for="fieldId">
      {{ label }}
      <span v-if="required" class="ar-field__required" aria-hidden="true">*</span>
    </label>
    <input
      :id="fieldId"
      class="ar-input"
      :aria-invalid="Boolean(error)"
      :aria-describedby="error ? errorId : helperText ? helperId : undefined"
      :aria-required="required"
      v-bind="$attrs"
    />
    <span v-if="error" :id="errorId" class="ar-field__error" role="alert">{{ error }}</span>
    <span v-else-if="helperText" :id="helperId" class="ar-field__helper">{{ helperText }}</span>
  </div>
</template>

<script setup>
import { computed, useId } from "vue";

// TextField — labeled input with helper text and error state.
// <TextField label="Work email" placeholder="you@company.com" required />
const props = defineProps({
  label: { type: String, default: "" },
  helperText: { type: String, default: "" },
  error: { type: String, default: "" },
  required: { type: Boolean, default: false },
  id: { type: String, default: "" },
});

const autoId = useId ? useId() : `field-${Math.random().toString(36).slice(2, 9)}`;
const fieldId = computed(() => props.id || autoId);
const helperId = computed(() => `${fieldId.value}-helper`);
const errorId = computed(() => `${fieldId.value}-error`);
</script>

<style>
@import "../../tokens/components.css";
</style>
