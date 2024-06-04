// vuetify 기본 설정

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'

export default createVuetify({
  components,
  directives,
  ssr: true,
  defaults: {
    // VBtn: {
    //   color: 'primary',
    //   variant: 'outlined',
    //   rounded: true,
    // },
  },
})
