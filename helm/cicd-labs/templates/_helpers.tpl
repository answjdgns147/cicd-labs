{{- define "cicd-labs.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
기존 k8s/ 매니페스트와 동일한 셀렉터 유지 (Deployment selector는 변경 불가)
*/}}
{{- define "cicd-labs.selectorLabels" -}}
app: {{ include "cicd-labs.name" . }}
{{- end }}

{{- define "cicd-labs.labels" -}}
{{ include "cicd-labs.selectorLabels" . }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
