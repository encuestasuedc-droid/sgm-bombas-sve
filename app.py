from flask import Flask, render_template_string

app = Flask(__name__)

# Guardamos todo tu diseño HTML y CSS dentro de una variable de Python segura
html_layout = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SGM Bombas SVE</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <style>
        * {
            box-sizing: border-box;
        }
        html, body {
            margin: 0;
            min-height: 100%;
        }
        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #f7f4ef;
        }
        .inicio-app {
            position: relative;
            display: grid;
            grid-template-columns: 47% 53%;
            min-height: 100vh;
            overflow: hidden;
            background: #faf8f4;
        }
        /* Círculo bordó superior */
        .inicio-app::before {
            content: "";
            position: absolute;
            z-index: 4;
            top: -230px;
            right: -170px;
            width: 500px;
            height: 360px;
            background: linear-gradient( 135deg, #771052, #4e0639 );
            border-radius: 50%;
            transform: rotate(14deg);
            pointer-events: none;
        }
        /* Círculo bordó inferior */
        .inicio-app::after {
            content: "";
            position: absolute;
            z-index: 4;
            bottom: -470px;
            left: -350px;
            width: 760px;
            height: 680px;
            background: linear-gradient( 145deg, #4e0639, #771052 );
            border: 14px solid #dfbedb;
            border-radius: 50%;
            transform: rotate(-15deg);
            pointer-events: none;
        }
        /* Columna izquierda */
        .panel-principal {
            position: relative;
            z-index: 5;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 65px 45px 120px max(45px, 8vw);
        }
        .etiqueta-sistema {
            align-self: flex-start;
            margin-bottom: 22px;
            padding: 7px 14px;
            color: white;
            background: #6b123c;
            border-radius: 30px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        }
        .logo-principal {
            display: block;
            width: min(340px, 85%);
            height: auto;
            margin-bottom: 20px;
            object-fit: contain;
            object-position: left center;
        }
        .descripcion-principal {
            max-width: 540px;
            margin: 0;
            color: #624957;
            font-size: 17px;
            line-height: 1.6;
        }
        /* Botones */
        .menu-principal {
            display: grid;
            gap: 14px;
            width: min(570px, 100%);
            margin-top: 38px;
        }
        .boton-menu {
            display: flex;
            align-items: center;
            gap: 18px;
            width: 100%;
            min-height: 92px;
            padding: 16px 20px;
            color: #5b0a43;
            text-decoration: none;
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid rgba(91, 10, 67, 0.16);
            border-radius: 18px;
            box-shadow: 0 12px 30px rgba(70, 15, 52, 0.13);
            transition: transform 0.2s ease, background 0.2s ease, color 0.2s ease, box-shadow 0.2s ease;
        }
        .boton-menu:hover {
            color: white;
            background: linear-gradient( 135deg, #771052, #4e0639 );
            transform: translateX(7px);
            box-shadow: 0 18px 38px rgba(70, 15, 52, 0.25);
        }
        .boton-icono {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            width: 60px;
            height: 60px;
            background: #f0dced;
            border-radius: 50%;
            font-size: 28px;
        }
        .boton-menu:hover .boton-icono {
            background: rgba(255, 255, 255, 0.17);
        }
        .boton-texto {
            display: block;
        }
        .boton-texto strong {
            display: block;
            font-size: 17px;
            line-height: 1.2;
            letter-spacing: 0.4px;
            text-transform: uppercase;
        }
        .boton-texto small {
            display: block;
            margin-top: 5px;
            font-size: 13px;
            opacity: 0.72;
        }
        /* Columna derecha con la fotografía */
        .panel-imagen {
            position: relative;
            z-index: 1;
            min-height: 100vh;
            overflow: hidden;
            background-color: #f7f3ef;
        }
        .panel-imagen::before {
            content: "";
            position: absolute;
            z-index: 2;
            inset: 0;
            background: linear-gradient( 90deg, #faf8f4 0%, rgba(250, 248, 244, 0.48) 12%, rgba(250, 248, 244, 0.04) 33%, rgba(250, 248, 244, 0) 100% );
            pointer-events: none;
        }
        .imagen-bombas {
            width: 100%;
            height: 100vh;
            object-fit: cover;
            object-position: center center;
            display: block;
        }
        /* Beneficios inferiores */
        .beneficios {
            position: absolute;
            z-index: 6;
            left: 50%;
            bottom: 16px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            width: min(920px, 70%);
            transform: translateX(-50%);
        }
        .beneficio {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 9px;
            min-height: 52px;
            padding: 10px 14px;
            color: white;
            background: rgba(82, 7, 60, 0.87);
            border: 1px solid rgba(255, 255, 255, 0.20);
            border-radius: 12px;
            text-align: center;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            backdrop-filter: blur(8px);
        }
        /* Tablet */
        @media (max-width: 950px) {
            .inicio-app {
                grid-template-columns: 1fr;
            }
            .panel-principal {
                min-height: auto;
                padding: 60px max(28px, 7vw) 40px;
                background: rgba(250, 248, 244, 0.93);
            }
            .logo-principal {
                width: min(300px, 80%);
            }
            .menu-principal {
                width: 100%;
            }
            .panel-imagen {
                min-height: 520px;
            }
            .imagen-bombas {
                height: 520px;
                object-position: center center;
            }
            .panel-imagen::before {
                background: linear-gradient( 180deg, #faf8f4 0%, rgba(250, 248, 244, 0.20) 20%, rgba(250, 248, 244, 0) 45% );
            }
            .beneficios {
                position: relative;
                left: auto;
                bottom: auto;
                grid-template-columns: 1fr;
                width: auto;
                padding: 14px 20px 25px;
                background: #4e0639;
                transform: none;
            }
        }
        /* Celular */
        @media (max-width: 600px) {
            .panel-principal {
                padding: 48px 20px 32px;
            }
            .inicio-app::before {
                top: -270px;
                right: -270px;
            }
            .inicio-app::after {
                display: none;
            }
            .logo-principal {
                width: min(270px, 86%);
            }
            .descripcion-principal {
                font-size: 15px;
            }
            .boton-menu {
                min-height: 82px;
                padding: 13px 15px;
            }
            .boton-icono {
                width: 54px;
                height: 54px;
                font-size: 25px;
            }
            .boton-texto strong {
                font-size: 15px;
            }
            .panel-imagen {
                min-height: 415px;
            }
            .imagen-bombas {
                height: 415px;
                object-position: 60% center;
            }
        }
    </style>
</head>
<body>
    <main class="inicio-app">
        <section class="panel-principal">
            <span class="etiqueta-sistema">SISTEMA SVE</span>
            <img class="logo-principal" src="/static/img/logo_sve.png" alt="Logo SGM SVE">
            <p class="descripcion-principal">
                Sistema de registro y seguimiento de mantenimientos para las bombas C1 a C23.
            </p>
            <nav class="menu-principal">
                <a href="/nuevo" class="boton-menu">
                    <span class="boton-icono">⚙️</span>
                    <span class="boton-texto">
                        <strong>Nuevo Registro</strong>
                        <small>Crear una nueva orden de mantenimiento</small>
                    </span>
                </a>
                <a href="/seguimiento" class="boton-menu">
                    <span class="boton-icono">📊</span>
                    <span class="boton-texto">
                        <strong>Seguimiento de Bombas</strong>
                        <small>Ver estados operativos de C1 a C23</small>
                    </span>
                </a>
                <a href="/historial" class="boton-menu">
                    <span class="boton-icono">📋</span>
                    <span class="boton-texto">
                        <strong>Historial General</strong>
                        <small>Buscar mantenimientos anteriores</small>
                    </span>
