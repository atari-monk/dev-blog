# SearchBar

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQR0wnxMBI3oSbWCQy1PzPP0ASLjaXm5RRt3J4tLhreXYTE" width="98" height="120" frameborder="0" scrolling="no"></iframe>

## Core Concepts

1. **Component Props**:
   - `filterText`: Current search text (string)
   - `inStockOnly`: Boolean for checkbox state
   - `onFilterTextChange`: Callback when text changes
   - `onInStockOnlyChange`: Callback when checkbox toggles

2. **Controlled Components**:
   - Input's `value` is controlled by `filterText` prop
   - Checkbox's `checked` is controlled by `inStockOnly` prop

3. **Event Handling**:
   - `onChange` for input calls parent callback with new text value
   - `onChange` for checkbox calls parent callback with new checked state

## How It Works

1. **Text Input**:
   - Displays current `filterText`
   - On keystroke, extracts new value from event (`e.target.value`)
   - Calls `onFilterTextChange` with new value

2. **Checkbox**:
   - Shows "Only show products in stock" label
   - Reflects current `inStockOnly` state
   - On toggle, extracts new state from event (`e.target.checked`)
   - Calls `onInStockOnlyChange` with new state

## Key React Patterns

- **Unidirectional Data Flow**: Parent component manages state, passes down via props
- **Lifting State Up**: Changes bubble up via callbacks to parent component
- **Single Source of Truth**: Form elements derive their values from props, not internal state
