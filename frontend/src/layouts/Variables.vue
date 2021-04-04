<template>
  <div class="q-pa-md justify='center'">

    <q-select
      filled
      v-model="model"
      use-input
      :options="options"
      label="Variables options"
      stack-label
      @input="getVariables"
      style="width: 10%; position: fixed; top: 10%; left: 45%"
      emit-value
      map-options
    />

    <q-table
      title="Variables"
      :data="variables"
      :columns="columns"
      row-key="name"
      style="width: 60%; position: fixed; top: 20%; left: 20%"
    />

  </div>

</template>

<script>

const arrayOptions = [
  { label: 'Boolean', value: 'boolean' },
  { label: 'String', value: 'string' }
]
import { api } from 'boot/variables'

export default {

  type_value: 'boolean',
  name: 'Variables',
  data () {
    return {
      model: null,
      options: arrayOptions,
      variables: [],
      columns: [
        {
          name: 'type',
          required: true,
          label: 'Type',
          align: 'left',
          field: row => row.type,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'name', align: 'center', label: 'Name', field: 'name', sortable: true },
        { name: 'value', label: 'Value', field: 'value', sortable: true },
      ],
    }
  },

  mounted () {
    this.getVariables(this.model)
  },
  methods: {

    getVariables (val) {

      if (this.model !== null) {
        var url = '/api/v1/'+ val

        api.get(url)
        .then((response) => {
          this.variables = response.data
        })
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem'
          })
        })
      }
    }
  }
}
</script>
