#include "plugin_utils.h"
#include "plugin.h"

// Called once to init.
void handle_init_contract(ethPluginInitContract_t *msg) {
    // Make sure we are running a compatible version.
    if (msg->interfaceVersion != ETH_PLUGIN_INTERFACE_VERSION_LATEST) {
        // If not the case, return the `UNAVAILABLE` status.
        msg->result = ETH_PLUGIN_RESULT_UNAVAILABLE;
        return;
    }

    // Double check that the `context_t` struct is not bigger than the maximum size (defined by
    // `msg->pluginContextLength`).
    if (msg->pluginContextLength < sizeof(context_t)) {
        PRINTF("Plugin parameters structure is bigger than allowed size\n");
        msg->result = ETH_PLUGIN_RESULT_ERROR;
        return;
    }

    context_t *context = (context_t *) msg->pluginContext;

    // Initialize the context (to 0).
    memset(context, 0, sizeof(*context));

    size_t index;
    if (!find_selector(U4BE(msg->selector, 0), SELECTORS, SELECTOR_COUNT, &index)) {
        PRINTF("Error: selector not found!\n");
        msg->result = ETH_PLUGIN_RESULT_UNAVAILABLE;
        return;
    }
    context->selectorIndex = index;
    // check for overflow
    if ((size_t) context->selectorIndex != index) {
        PRINTF("Error: overflow detected on selector index!\n");
        msg->result = ETH_PLUGIN_RESULT_ERROR;
        return;
    }

    // Set `next_param` to be the first field we expect to parse.
    // EDIT THIS: Adapt the `cases`, and set the `next_param` to be the first parameter you expect
    // to parse.
    switch (context->selectorIndex) {
        case GAIN_DEPOSIT_LST:
        case KELP_LST_DEPOSIT:
            context->next_param = TOKEN_ADDR;
            break;

        case GAIN_DEPOSIT_ETH:
        case KELP_ETH_DEPOSIT:
            context->next_param = UNEXPECTED_PARAMETER;
            break;

        case KELP_INITIATE_WITHDRAW:
            context->next_param = TOKEN_ADDR;
            break;

        case KELP_CLAIM_WITHDRAW:
            context->next_param = TOKEN_ADDR;
            break;

        case GAIN_DEPOSIT_RSETH:
            context->next_param = STAKE_AMOUNT;
            strlcpy(context->ticker, "rsETH", sizeof(context->ticker));
            break;

        case GAIN_WITHDRAW:
            context->next_param = UNSTAKE_AMOUNT;
            break;

        // Keep this
        default:
            PRINTF("Missing selectorIndex: %d\n", context->selectorIndex);
            msg->result = ETH_PLUGIN_RESULT_ERROR;
            return;
    }

    // Return valid status.
    msg->result = ETH_PLUGIN_RESULT_OK;
}
