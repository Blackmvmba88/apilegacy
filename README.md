# API Legacy — BlackMamba

**Repositorio madre para la capa legal, de seguridad, privacidad y trazabilidad de los programas BlackMamba.**

> Estado: `v0.1-alpha` — estructura operativa en construcción. Los documentos de este repositorio son plantillas técnicas y jurídicas de trabajo y deben revisarse con asesoría profesional antes de explotación comercial o contratación de alto riesgo.

## Objetivo

Todo programa BlackMamba debe poder nacer con una base común que responda, desde el primer commit:

- quién es el titular del proyecto;
- qué licencia aplica;
- qué datos procesa;
- qué API o interfaces expone;
- qué conductas de uso están permitidas o prohibidas;
- qué dependencias y marcas de terceros utiliza;
- cómo se reportan vulnerabilidades;
- qué versión exacta fue liberada;
- qué hash y commit identifican esa versión.

## Arquitectura

```text
apilegacy/
├── README.md
├── LICENSE
├── legal/
│   ├── API_TERMS.md
│   ├── PRIVACY_POLICY.md
│   ├── ACCEPTABLE_USE_POLICY.md
│   ├── DATA_RETENTION_POLICY.md
│   └── THIRD_PARTY_NOTICES.md
├── security/
│   └── SECURITY.md
├── manifests/
│   └── legal-manifest.example.yaml
├── templates/
│   └── project.template.json
└── docs/
    └── MEXICO_BASELINE.md
```

## Principio BlackMamba

```text
README   -> ingeniería
SPEC     -> comportamiento
SECURITY -> protección
LEGAL    -> derechos y obligaciones
MANIFEST -> identidad verificable
RELEASE  -> versión exacta
```

## Uso previsto

Este repo será la fuente base para generar o incorporar la carpeta legal de proyectos como apps, APIs, bridges, herramientas web, automatizaciones, controladores y software distribuido por BlackMamba.

## Regla de mínima recolección

Por defecto, un proyecto debe procesar **la menor cantidad de datos posible**. Si una función puede operar sin nombre, correo, ubicación, historial personal u otros datos identificables, esos datos no deben recolectarse.

## Cumplimiento

La base mexicana de privacidad se revisará contra la **Ley Federal de Protección de Datos Personales en Posesión de los Particulares vigente**, publicada mediante decreto en el DOF el 20 de marzo de 2025. La protección de marca se documentará con referencia al IMPI y el registro de software con referencia a INDAUTOR.

## Estado de esta versión

`v0.1-alpha` establece el esqueleto. Próximas capas:

- generador automático de paquete legal por proyecto;
- manifest firmado/hash por release;
- matriz de datos y finalidades;
- inventario de dependencias/licencias;
- checklist de publicación;
- plantillas de términos comerciales;
- integración CI para validar que cada release tenga su documentación legal mínima.
