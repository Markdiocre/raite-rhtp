import { Router, Response, Request } from "express";
// import { AccountRouter } from "../controller/Accounts";
import { Auth } from "../middleware/auth";
import { ProviderAvailController } from "../controller/ProviderController";
export const router: Router = Router();

// router.use("/accounts", AccountRouter);

router.get("/test", Auth, (req: Request, res: Response) => {
  res.send({ sample: "hi" });
});
router.use("/ProviderAvail", ProviderAvailController);
export const apiRouter: Router = router;
