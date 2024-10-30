## Obtencion de datos de carga de capacitor 
## equipo 2: 10 seg 

#include <stdio.h>
#include "string.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "driver/gpio.h"
#include "driver/uart.h"

#define UART_PORT UART_NUM_1
#define BUF_SIZE 1024 
#define TASK_MEMORY 2028
#define TXD_PIN GPIO_NUM_1
#define RXD_PIN GPIO_NUM_3

static const char *TAG = "UART";
#define LedR 14
#define LedG 12
#define LedB 13

esp_err_t uart_initialize();

static void uart_task(void *pvParameters)
{
uint8_t *data = (uint8_t *) malloc(BUF_SIZE); //puntero para almacenar la data que llega

    while (true) {
        /* Clear space memory */
        bzero(data, BUF_SIZE); //Borramos el espacio de memoria que este en data

        /* Read data from the UART */
        int len = uart_read_bytes(UART_PORT, data, BUF_SIZE, pdMS_TO_TICKS(100));
        if (len==0) //si el tamaño de lo que llego es cero, continua
        {
            continue;
        }
        // si es diferente de cero lo volvemos a leer
        /* Write data back to the UART */
        uart_write_bytes(UART_PORT, (const char *) data, len);
 
        ESP_LOGI(TAG, "Data recived: %s",data); //imprimimos en consola lo que acaba de llegar

        for (size_t i=0; i < len -2; i++) //for por cada elemento que llegue en Data y quitamos salto de /r/n
        {
            char value = data[i];

            switch (value)
            {
            case 'R':
                gpio_set_level(LedR,1);
                gpio_set_level(LedG,0);
                gpio_set_level(LedB,0);
                break;

            case 'G':
                gpio_set_level(LedR,0);
                gpio_set_level(LedG,1);
                gpio_set_level(LedB,0);
                break;

            case 'B':
                gpio_set_level(LedR,0);
                gpio_set_level(LedG,0);
                gpio_set_level(LedB,1);
                break;
            
            default:
                gpio_set_level(LedR,0);
                gpio_set_level(LedG,0);
                gpio_set_level(LedB,0);
                break;
            }

        }
    }
}

static void init_led(void)
{
    gpio_reset_pin(LedR);
    gpio_set_direction(LedR, GPIO_MODE_OUTPUT);
    gpio_reset_pin(LedG);
    gpio_set_direction(LedG, GPIO_MODE_OUTPUT);
    gpio_reset_pin(LedB);
    gpio_set_direction(LedB, GPIO_MODE_OUTPUT);

    //ESP_LOGI(TAG, "Init led completed");
}


esp_err_t uart_initialize(){
    const uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    };

    // We won't use a buffer for sending data.
    ESP_ERROR_CHECK(uart_driver_install(UART_PORT, BUF_SIZE, 0, 0, NULL, 0));
    ESP_ERROR_CHECK(uart_param_config(UART_PORT, &uart_config));
    ESP_ERROR_CHECK(uart_set_pin(UART_PORT, TXD_PIN, RXD_PIN, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE));

    return ESP_OK;
}

void app_main(){
    init_led();
    uart_initialize(); 
}